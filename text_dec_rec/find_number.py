import os
import sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../..')))

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import cv2
import copy
import numpy as np
import time
from PIL import Image
import tools.infer.utility as utility
import tools.infer.predict_rec as predict_rec
import tools.infer.predict_det as predict_det
import tools.infer.predict_cls as predict_cls
from ppocr.utils.utility import get_image_file_list, check_and_read_gif
from ppocr.utils.logging import get_logger
from tools.infer.utility import draw_ocr_box_txt
from tools.infer.predict_system import TextSystem

logger = get_logger()
args = utility.parse_args()


def det_and_rec_num(img):
    h, w = img.shape[:2]
    if h < 32 or w < 32:
        return -1
    text_sys = TextSystem(args)
    num = []
    dt_boxes, rec_res = text_sys(img)
    if rec_res != []:
        for text, score in rec_res:
            if text.isdigit():
                num.append(int(text))
    if len(num) == 1:
        return num[0]
    elif len(num) > 1:
        return -2
    else:
        return -1

        # print(text)


if __name__ == "__main__":
    img = cv2.imread('../imgs/others/1_2.png')
    print(det_and_rec_num(img))
