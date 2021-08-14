from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import deque
import numpy as np
import torch
import yolo
import aligned
from pysot.core.config import cfg
from pysot.models.model_builder import ModelBuilder
from pysot.tracker.tracker_builder import build_tracker
from text_dec_rec import find_number


class MyTracker():
    def __init__(self):
        self.num_init = 0  # 记录球员号码
        self.img_roi = None
        self.score = 0.9
        self.bbox = []
        self.scale_size = 600
        self.frame_count = 0
        # 保存  中心点的xy坐标
        self.memory_cx = deque(maxlen=2)
        self.memory_cy = deque(maxlen=2)
        # 标志位 有跟错情况发生
        self.flag_wrong = 0
        self.first_frame = True
        self.detection_frame = False
        self.multi_object_flag = False
        self.detection_obj = False
        self.detection_full = False
        # 加载yolo模型
        self.yolo_cfg = '../yolov4/yolov4.cfg'
        self.yolo_weight = '../yolov4/yolov4.weights'
        self.m_yolo = yolo.YOLO(self.yolo_cfg, self.yolo_weight, use_cuda=True)
        # 加载reid模型
        self.m_reid = aligned.AligedReid(use_cuda=True)
        # 加载跟踪模型
        self.track_cfg = '../pysot/experiments/siamrpn_r50_l234_dwxcorr/config.yaml'
        self.track_model = '../pysot/experiments/siamrpn_r50_l234_dwxcorr/model.pth'
        cfg.merge_from_file(self.track_cfg)
        cfg.CUDA = torch.cuda.is_available() and cfg.CUDA
        device = torch.device('cuda' if cfg.CUDA else 'cpu')
        model = ModelBuilder()
        model.load_state_dict(torch.load(self.track_model, map_location=lambda storage, loc: storage.cpu()))
        model.eval().to(device)
        self.tracker = build_tracker(model)

    def getROI(self, frame, init_rect):
        img_roi = frame[int(init_rect[1]):int(init_rect[1] + init_rect[3]),
                  int(init_rect[0]):int(init_rect[0] + init_rect[2])]
        return img_roi

    def updateTarget_num(self, img_roi, frame, init_num):
        cropimg, bboxs = self.m_yolo.detect_cv2(frame)
        # cropimg, bboxs = colorselect(img_roi, cropimg, bboxs)
        d, new_target_bbox = self.m_reid.target_match_fun_num(img_roi, cropimg, bboxs, init_num)
        return d, new_target_bbox

    def updateTarget(self, img_roi, frame):
        cropimg, bboxs = self.m_yolo.detect_cv2(frame)
        # cropimg, bboxs = colorselect(img_roi, cropimg, bboxs)
        d, new_target_bbox = self.m_reid.target_match_fun(img_roi, cropimg, bboxs)
        return d, new_target_bbox

    def updateTarget_deux(self, img_roi, img_current, frame):
        cropimg, bboxs = self.m_yolo.detect_cv2(frame)
        d, new_target_bbox = self.m_reid.target_match_fun_deux(img_roi, img_current, cropimg, bboxs)
        return d, new_target_bbox

    def initframe(self, frame, init_rect):
        # init_rect1 = [int(int(i) * 1.2) for i in init_rect]
        init_rect1 = list(init_rect)
        init_rect1[0] = int(init_rect1[0] - init_rect1[2] * 0.2)
        init_rect1[1] = int(init_rect1[1] - init_rect1[3] * 0.3)
        init_rect1[2] = int(init_rect1[2] * 1.6)
        init_rect1[3] = int(init_rect1[3] * 1.4)
        if init_rect1[0] < 0:
            init_rect1[0] = max(init_rect1[0], 0)
        if init_rect1[1] < 0:
            init_rect1[1] = max(init_rect1[1], 0)

        img_roi = frame[int(init_rect1[1]): int(min((init_rect1[1] + init_rect1[3]), 1080)),
                  int(init_rect1[0]): int(min((init_rect1[0] + init_rect1[2]), 1920))]
        num = find_number.det_and_rec_num(img_roi)

        return img_roi, num

    def initbox_scale(self, init_rect):

        cx = init_rect[0] + init_rect[2] / 2
        cy = init_rect[1] + init_rect[3] / 2
        w = init_rect[2] * 0.9
        h = init_rect[3] * 0.8

        init_rect[0] = int(cx - w / 2)
        init_rect[1] = int(cy - h / 2)
        init_rect[2] = int(w)
        init_rect[3] = int(h)

        return init_rect

    def find_local_frame(self, memory_cx, memory_cy, frame):
        c_x = memory_cx[1]
        c_y = memory_cy[1]
        x_start = c_x - self.scale_size
        y_start = c_y - self.scale_size
        x_end = c_x + self.scale_size
        y_end = c_y + self.scale_size
        if c_x - self.scale_size <= 0:
            x_start = 0
        if c_y - self.scale_size <= 0:
            y_start = 0
        if c_x + self.scale_size >= 1920:
            x_end = 1920
        if c_y + self.scale_size >= 1080:
            y_end = 1080
        img_1 = frame[int(y_start): int(y_end), int(x_start): int(x_end)]
        return img_1, x_start, y_start

    def scale_rect(self, init_rect):
        cx = init_rect[0] + init_rect[2] / 2
        cy = init_rect[1] + init_rect[3] / 2
        w = init_rect[2] * 0.8
        h = init_rect[3] * 0.8

        init_rect[0] = int(cx - w / 2)
        init_rect[1] = int(cy - h / 2)
        init_rect[2] = int(w)
        init_rect[3] = int(h)

        return init_rect

    def init(self, img, gt_bbox, num):
        self.score = 0.9
        gt_bbox = self.initbox_scale(gt_bbox)
        self.img_roi, self.num_init = self.initframe(img, gt_bbox)
        if self.num_init == -1 or self.num_init == -2:
            print(' Numbers are blurred and cannot be read , pl input ')
            num_init = num
            print('     *****  num_init - - - - - : ', num_init, '   ******')
        self.tracker.init(img, gt_bbox)  # 127 * 127

        self.memory_cx.append((gt_bbox[0] + gt_bbox[2] / 2))
        self.memory_cy.append((gt_bbox[1] + gt_bbox[3] / 2))
        self.detection_frame = False
        self.memory_cy_flag = 0
        self.memory_cx_flag = 0

    def track(self, frame):
        if self.frame_count % 149 == 0:
            self.frame_count = 0

        outputs = {}
        while True:
            if self.frame_count > 3 and (self.memory_cy_flag > 35 or self.memory_cx_flag > 45):
                print('**************************************************************************/n')
                print('wrong tracking  --  big diff x_cneter y_center  ** multi_object_flag is True')
                print('**************************************************************************/n')
                self.multi_object_flag = True
            if self.flag_wrong == 20:
                print('Flag wrong : detection_frame = True')
                self.flag_wrong = 0
                self.detection_frame = True
                self.multi_object_flag = False

            if self.multi_object_flag:
                self.flag_wrong += 1

            if self.score < 0.2:
                print('Score contrll : detection_score < 0.4 detection wrong full is True')
                self.detection_full = True
            self.frame_count += 1
            if self.detection_frame:
                print('Entrer  :  detection_local_frame part')
                img_1, x_start, y_start = self.find_local_frame(self.memory_cx, self.memory_cy, frame)
                _, new_target_bbox = self.updateTarget(self.img_roi, img_1)

                self.detection_frame = False
                self.score = 0.9

                # 重新初始化
                new_target_bbox[0] = new_target_bbox[0] + x_start
                new_target_bbox[1] = new_target_bbox[1] + y_start
                init_rect = new_target_bbox  # 这里要放新的 bbox

                # 差分计算
                self.memory_cx.append((init_rect[0] + init_rect[2] / 2))
                self.memory_cy.append((init_rect[1] + init_rect[3] / 2))
                self.memory_cx.append((init_rect[0] + init_rect[2] / 2))
                self.memory_cy.append((init_rect[1] + init_rect[3] / 2))

                init_rect_scale = self.scale_rect(init_rect)
                self.tracker.init_center_pos(init_rect_scale)
                print('Local detection : detection done! continue tracking !')
                outputs['bbox'] = init_rect
                outputs['best_score'] = 0.9
            elif self.detection_obj:
                print('Detecte current object : ')
                self.detection_obj = False
                img_now = frame[int(self.bbox[1]): int(self.bbox[1] + self.bbox[3]),
                          int(self.bbox[0]): int(self.bbox[0] + self.bbox[2])]
                num = find_number.det_and_rec_num(img_now)
                print('     Current object : number_now  -- ***** -- ', num)
                if num != self.num_init or num == -1 or num == -2:
                    print('     wrong tracking')
                    self.detection_full = True
                if num == self.num_init:
                    init_rect_scale = self.scale_rect(self.bbox)
                    img_now_scale = frame[int(init_rect_scale[1]): int(init_rect_scale[1] + init_rect_scale[3]),
                                    int(init_rect_scale[0]): int(init_rect_scale[0] + init_rect_scale[2])]
                    self.tracker.init(frame, init_rect_scale)
                outputs['bbox'] = self.bbox
                outputs['best_score'] = 0.9
            elif self.detection_full:
                print('Entrer : detection full')
                self.detection_full = False
                self.score = 0.9

                _, new_target_bbox = self.updateTarget(self.img_roi, frame)

                img_now = frame[int(new_target_bbox[1]): int(new_target_bbox[1] + new_target_bbox[3]),
                          int(new_target_bbox[0]): int(new_target_bbox[0] + new_target_bbox[2])]
                num = find_number.det_and_rec_num(img_now)
                print('     Detection full : detection_full_number_now - - ****  - ', num)
                if num != self.num_init or num == -1 or num == -2:
                    self.multi_object_flag = True
                if num == self.num_init:
                    init_rect_scale = self.scale_rect(new_target_bbox)
                    img_now_scale = frame[int(init_rect_scale[1]): int(init_rect_scale[1] + init_rect_scale[3]),
                                    int(init_rect_scale[0]): int(init_rect_scale[0] + init_rect_scale[2])]
                    self.tracker.init(frame, init_rect_scale)

                self.memory_cx.append((new_target_bbox[0] + new_target_bbox[2] / 2))
                self.memory_cy.append((new_target_bbox[1] + new_target_bbox[3] / 2))
                self.memory_cx.append((new_target_bbox[0] + new_target_bbox[2] / 2))
                self.memory_cy.append((new_target_bbox[1] + new_target_bbox[3] / 2))

                init_rect_scale = self.scale_rect(new_target_bbox)
                self.tracker.init_center_pos(init_rect_scale)

                outputs['bbox'] = new_target_bbox
                outputs['best_score'] = 0.9

            else:
                outputs = self.tracker.track(frame)
                self.bbox = list(map(int, outputs['bbox']))
                self.score = outputs['best_score']
                # if self.frame_count % 150 == 1:
                #     print('****************************************************/n')
                #     print('Frame count = 150 :  ******  - -detection_obj = True')
                #     print('****************************************************/n')
                #     self.detection_obj = True
                self.memory_cx.append(self.bbox[4])
                self.memory_cy.append(self.bbox[5])

                # break
            self.memory_cx_flag = np.abs(self.memory_cx[-1] - self.memory_cx[0])
            self.memory_cy_flag = np.abs(self.memory_cy[-1] - self.memory_cy[0])
            print('count -- ', self.frame_count, '     memory_cx_flag', ' -- ', self.memory_cx_flag,
                  ' -- ', 'memory_cx_flag', ' -- ', self.memory_cy_flag, 'score -- ', self.score)
            break
        return outputs
