# -*- coding: utf-8 -*-

from yolov4.tool.utils import *
from yolov4.tool.torch_utils import *
from yolov4.tool.darknet2pytorch import Darknet

import cv2

"""hyper parameters"""


class YOLO():

    def __init__(self, cfgfile, weightfile, use_cuda=False):
        self.m = Darknet(cfgfile)
        self.m.load_weights(weightfile)
        self.use_cuda = use_cuda
        if use_cuda:
            self.m.cuda()

        num_classes = 1
        # num_classes = self.m.num_classes
        if num_classes == 20:
            namesfile = '../yolov4/voc.names'
        elif num_classes == 80:
            namesfile = '../yolov4/coco.names'
        else:
            namesfile = '../yolov4/person.names'
        self.class_names = load_class_names(namesfile)

    def detect_cv2(self, imgfile):

        sized = cv2.resize(imgfile, (self.m.width, self.m.height))
        sized = cv2.cvtColor(sized, cv2.COLOR_BGR2RGB)
        if self.use_cuda:
            imgfile = torch.from_numpy(imgfile)
            imgfile = imgfile.cuda()
        for i in range(2):
            boxes = do_detect(self.m, sized, 0.3, 0.6, self.use_cuda)

        _, cropimg, bboxs = plot_boxes_cv2(imgfile, boxes[0], savename=None, class_names=self.class_names)

        return cropimg, bboxs
