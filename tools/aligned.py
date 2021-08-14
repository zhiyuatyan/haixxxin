from reid.util.FeatureExtractor import FeatureExtractor
from torchvision import transforms
from reid import models
from scipy.spatial.distance import euclidean
from reid.util.utils import *
from sklearn.preprocessing import normalize
import os
from PIL import Image

from text_dec_rec import find_number


class AligedReid():

    def __init__(self, use_cuda=False):
        self.use_cuda = use_cuda
        os.environ['CUDA_VISIBLE_DEVICES'] = "0"
        self.model = models.init_model(name='resnet50', num_classes=751, loss={'softmax', 'metric'},
                                       use_gpu=self.use_cuda,
                                       aligned=True)
        checkpoint = torch.load("../reid/checkpoint_ep300.pth.tar")
        self.model.load_state_dict(checkpoint['state_dict'])
        if self.use_cuda:
            self.model = self.model.cuda()
        self.img_transform = transforms.Compose([
            transforms.Resize((256, 128)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        exact_list = ['7']
        self.myexactor = FeatureExtractor(self.model, exact_list)

    def pool2d(self, tensor, type='max'):
        sz = tensor.size()
        if type == 'max':
            x = torch.nn.functional.max_pool2d(tensor, kernel_size=(int(sz[2] / 8), sz[3]))
        if type == 'mean':
            x = torch.nn.functional.mean_pool2d(tensor, kernel_size=(sz[2] / 8, sz[3]))
        x = x[0].cpu().data.numpy()
        x = np.transpose(x, (2, 1, 0))[0]
        return x

    def target_match_fun(self, target, det_frames, boxes):
        # 初始化
        target = Image.fromarray(target)
        i = 0
        for data in det_frames:
            det_frames[i] = Image.fromarray(det_frames[i])
            i = i + 1

        idex = []
        for img2 in det_frames:
            img1 = img_to_tensor(target, self.img_transform)
            img2 = img_to_tensor(img2, self.img_transform)
            if self.use_cuda:
                img1 = img1.cuda()
                img2 = img2.cuda()
            self.model.eval()
            f1 = self.myexactor(img1)
            f2 = self.myexactor(img2)
            a1 = normalize(self.pool2d(f1[0], type='max'))
            a2 = normalize(self.pool2d(f2[0], type='max'))
            dist = np.zeros((8, 8))
            for i in range(8):
                temp_feat1 = a1[i]
                for j in range(8):
                    temp_feat2 = a2[j]
                    dist[i][j] = euclidean(temp_feat1, temp_feat2)
            d, D, sp = dtw(dist)
            idex.append(d)
            # print('min_distance : ',min(idex))
        if len(idex) == 0:
            return -1, []
        else:
            return min(idex), boxes[idex.index(min(idex))]

    def target_match_fun_num(self, target, det_frames, boxes, init_num):
        # 初始化
        target = Image.fromarray(target)
        det_frames_new = []
        num = []
        boxes_new = []
        i = 0
        j = 0
        for data in det_frames:

            if det_frames[i].shape[0] <= 0 or det_frames[i].shape[1] <= 0:
                i += 1
                continue
            num_now = find_number.det_and_rec_num(data)
            num.append(num_now)
            if num_now != init_num and num_now != -1 and num_now != -2:
                i += 1
                continue

            det_frames_new.append(Image.fromarray(det_frames[i]))
            boxes_new.append(boxes[i])
            j += 1
            i += 1

        use_gpu = torch.cuda.is_available()
        model = models.init_model(name='resnet50', num_classes=751, loss={'softmax', 'metric'}, use_gpu=use_gpu,
                                  aligned=True)
        checkpoint = torch.load("checkpoint_ep300.pth.tar")
        model.load_state_dict(checkpoint['state_dict'])

        img_transform = transforms.Compose([
            transforms.Resize((256, 128)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        exact_list = ['7']
        myexactor = FeatureExtractor(model, exact_list)

        idex = []
        img1 = img_to_tensor(target, img_transform)
        f1 = myexactor(img1)
        a1 = normalize(self.pool2d(f1[0], type='max'))
        if use_gpu:
            img1 = img1.cuda()
        for img2 in det_frames_new:

            img2 = img_to_tensor(img2, img_transform)
            if use_gpu:
                model = model.cuda()
                img2 = img2.cuda()
            model.eval()
            f2 = myexactor(img2)
            a2 = normalize(self.pool2d(f2[0], type='max'))
            dist = np.zeros((8, 8))
            for i in range(8):
                temp_feat1 = a1[i]
                for j in range(8):
                    temp_feat2 = a2[j]
                    dist[i][j] = euclidean(temp_feat1, temp_feat2)
            d, D, sp = dtw(dist)
            idex.append(d)

        return d, boxes_new[idex.index(min(idex))]
