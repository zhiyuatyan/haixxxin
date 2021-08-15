# Copyright (c) SenseTime. All Rights Reserved.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from video_dispaly import Ui_MainWindow

import init_arg
from collections import deque
from threading import Thread
import kuashidian
from tools.tracker import MyTracker

import cv2

init_rect = []


class myLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    def mousePressEvent(self, event):
        # self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    def mouseReleaseEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def clear(self):
        self.flag = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag:
            rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
            painter.drawRect(rect)

            global init_rect
            init_rect = [self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0)]
        # self.update()


class Video_Dis(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Video_Dis, self).__init__(parent)
        self.setupUi(self)
        self.open_video.clicked.connect(self.openVideo)
        self.pushButton.clicked.connect(self.on_video)
        self.select_player.clicked.connect(self.select_ROI)
        self.start.clicked.connect(self.confirm_player)
        self.comboBox.currentIndexChanged.connect(
            lambda: self.WrittingNotOfOther(self.comboBox.currentIndex()))  # 点击下拉列表，触发对应事件

        self.push0.clicked.connect(lambda: self.videochange(0))
        self.push1.clicked.connect(lambda: self.videochange(1))
        self.push2.clicked.connect(lambda: self.videochange(2))
        self.push3.clicked.connect(lambda: self.videochange(3))
        self.push4.clicked.connect(lambda: self.videochange(4))
        self.push5.clicked.connect(lambda: self.videochange(5))
        self.push6.clicked.connect(lambda: self.videochange(6))
        self.push7.clicked.connect(lambda: self.videochange(7))
        self.push8.clicked.connect(lambda: self.videochange(8))
        self.push9.clicked.connect(lambda: self.videochange(9))

        self.args = init_arg.args()
        self.pred_bbox = []
        self.save_view_2 = deque(maxlen=2)
        self.push_buttom = 0
        self.frame_count = 0
        self.video_display = None

        # 跟踪需要的flag
        self.select_player_flag = False  # 选择球员
        self.track_flag = False  # 跟踪标志，开始或暂停
        self.first_frame = False
        self.video_change_flag = False

        self.tag_flag = 0
        self.save_view_2.append(0)
        self.painter = QPainter(self)

        self.initUI()
        self.tracker = None

    # 清除label对象的绘制内容
    def clearRect(self):
        self.play_label.clear()

    def printRect(self):
        self.play_label.flag = True

    def loadTracker(self):
        self.tracker = MyTracker()
        print("tracker加载成功！！！")

    def initUI(self):
        self.play_label = myLabel(self)

        # 对于重新修改的Qlabel  * 自定义事件

        self.play_label.setGeometry(QtCore.QRect(320, 30, 640, 480))
        self.play_label.setStyleSheet("border-width: 1px;\n"
                                      "border-style: solid;\n"
                                      "border-color: #6633FF;\n"
                                      "")
        self.play_label.setFrameShape(QtWidgets.QFrame.Box)
        self.play_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.play_label.setLineWidth(3)
        self.play_label.setMidLineWidth(0)
        self.play_label.setObjectName("play_label")
        # 新建线程加载跟踪模型
        t = Thread(target=self.loadTracker)
        t.start()

    def btnInit(self):
        self.first_frame = True
        self.select_player.setEnabled(True)
        self.select_player.setText("选择球员")
        self.start.setEnabled(True)
        self.start.setText("跟踪器初始化")

    def openVideo(self):
        fileDialog = QFileDialog()
        # 设置可以打开任何文件
        fileDialog.setFileMode(QFileDialog.AnyFile)
        # 打开文件选取的窗口，并返回文件路径
        videoPath, _ = fileDialog.getOpenFileName(self.open_video, 'open file', './', )  #
        if not videoPath:
            QMessageBox.warning(self.open_video, "警告", "文件错误或打开文件失败！", QMessageBox.Yes)
            return
        self.video_display = cv2.VideoCapture(videoPath)
        print("读入文件成功")
        self.btnInit()
        self.update()

    def on_video(self):
        if self.track_flag:
            self.pushButton.setText('开始跟踪')

        else:
            self.pushButton.setText('暂停跟踪')
        self.track_flag = bool(1 - self.track_flag)

    def confirm_player(self):
        self.start.setText('正在初始化')
        t = Thread(target=self.trackerInit)
        t.start()
        # self.trackerInit()

    def trackerInit(self):
        print('current :', init_rect)
        self.current_player = frame_copy[int(init_rect[1]):int(init_rect[1] + init_rect[3]),
                              int(init_rect[0]):int(init_rect[0] + init_rect[2])]

        self.tracker.init(frame_copy, init_rect, 30)
        print('done')
        self.start.setText('初始化完成')
        self.start.setEnabled(False)

    def select_ROI(self):
        self.printRect()
        if self.select_player_flag:
            self.select_player.setText('select')
        else:
            self.select_player.setText('球员已确定')
            self.select_player.setEnabled(False)
        self.select_player_flag = bool(1 - self.select_player_flag)

    def showPic(self, frame):
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.Qframe = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3,
                             QImage.Format_RGB888)
        self.play_label.setPixmap(QPixmap.fromImage(self.Qframe))

    def videochange(self, pushbuttom):
        self.video_change_flag = True

        if self.tag_flag == 0:
            self.save_view_2.append(pushbuttom)
            if pushbuttom == 0:
                self.video_display = cv2.VideoCapture(self.args.video_name0)
                print('0 push')
            if pushbuttom == 1:
                self.video_display = cv2.VideoCapture(self.args.video_name1)
                print('1 push')
            if pushbuttom == 2:
                self.video_display = cv2.VideoCapture(self.args.video_name2)
                print('2 push')
            if pushbuttom == 3:
                self.video_display = cv2.VideoCapture(self.args.video_name3)
                print('3 push')
            if pushbuttom == 4:
                self.video_display = cv2.VideoCapture(self.args.video_name4)
                print('4 push')
            if pushbuttom == 5:
                self.video_display = cv2.VideoCapture(self.args.video_name5)
                print('5 push')
            if pushbuttom == 6:
                self.push_buttom = 6
                self.video_display = cv2.VideoCapture(self.args.video_name6)
                print('6 push')
            if pushbuttom == 7:
                self.push_buttom = 7
                self.video_display = cv2.VideoCapture(self.args.video_name7)
                print('7 push')
            if pushbuttom == 8:
                self.push_buttom = 8
                self.video_display = cv2.VideoCapture(self.args.video_name8)
                print('8 push')
            if pushbuttom == 9:
                self.push_buttom = 9
                self.video_display = cv2.VideoCapture(self.args.video_name9)
                print('9 push')
        elif self.tag_flag == 1:
            self.save_view_2.append(pushbuttom + 10)
            if pushbuttom == 0:
                self.video_display = cv2.VideoCapture(self.args.video_name10)
                print('10 push')
            if pushbuttom == 1:
                self.video_display = cv2.VideoCapture(self.args.video_name11)
                print('11 push')
            if pushbuttom == 2:
                self.video_display = cv2.VideoCapture(self.args.video_name12)
                print('12 push')
            if pushbuttom == 3:
                self.video_display = cv2.VideoCapture(self.args.video_name13)
                print('13 push')
            if pushbuttom == 4:
                self.video_display = cv2.VideoCapture(self.args.video_name14)
                print('14 push')
            if pushbuttom == 5:
                self.video_display = cv2.VideoCapture(self.args.video_name15)
                print('15 push')
            if pushbuttom == 6:
                self.video_display = cv2.VideoCapture(self.args.video_name16)
                print('16 push')
            if pushbuttom == 7:
                self.video_display = cv2.VideoCapture(self.args.video_name17)
                print('17 push')
            if pushbuttom == 8:
                self.video_display = cv2.VideoCapture(self.args.video_name18)
                print('18 push')
            if pushbuttom == 9:
                self.video_display = cv2.VideoCapture(self.args.video_name19)
                print('19 push')
        elif self.tag_flag == 2:
            self.save_view_2.append(pushbuttom + 20)
            if pushbuttom == 0:
                self.video_display = cv2.VideoCapture(self.args.video_name20)
                print('20 push')
            if pushbuttom == 1:
                self.video_display = cv2.VideoCapture(self.args.video_name21)
                print('21 push')
            if pushbuttom == 2:
                self.video_display = cv2.VideoCapture(self.args.video_name22)
                print('22 push')
            if pushbuttom == 3:
                self.video_display = cv2.VideoCapture(self.args.video_name23)
                print('23 push')
            if pushbuttom == 4:
                self.video_display = cv2.VideoCapture(self.args.video_name24)
                print('24 push')
            if pushbuttom == 5:
                self.video_display = cv2.VideoCapture(self.args.video_name25)
                print('25 push')
            if pushbuttom == 6:
                self.video_display = cv2.VideoCapture(self.args.video_name26)
                print('26 push')
            if pushbuttom == 7:
                self.video_display = cv2.VideoCapture(self.args.video_name27)
                print('27 push')
            if pushbuttom == 8:
                self.video_display = cv2.VideoCapture(self.args.video_name28)
                print('28 push')
            if pushbuttom == 9:
                self.video_display = cv2.VideoCapture(self.args.video_name29)
                print('29 push')
        print('Button {0} clicked'.format(pushbuttom))
        self.update()

    # 下拉菜单
    def WrittingNotOfOther(self, tag):
        if tag == 0:
            self.tag_flag = 0
            self.push0.setText("视角0")
            self.push1.setText('视角1')
            self.push2.setText("视角2")
            self.push3.setText('视角3')
            self.push4.setText('视角4')
            self.push5.setText('视角5')
            self.push6.setText('视角6')
            self.push7.setText('视角7')
            self.push8.setText('视角8')
            self.push9.setText('视角9')

        if tag == 1:
            self.tag_flag = 1
            print('点到了第1项 ...')
            self.push0.setText("视角10")
            self.push1.setText('视角11')
            self.push2.setText("视角12")
            self.push3.setText('视角13')
            self.push4.setText('视角14')
            self.push5.setText('视角15')
            self.push6.setText('视角16')
            self.push7.setText('视角17')
            self.push8.setText('视角18')
            self.push9.setText('视角19')
        if tag == 2:
            self.tag_flag = 2
            print('点到了第2项 ...')
            self.push0.setText("视角20")
            self.push1.setText('视角21')
            self.push2.setText("视角22")
            self.push3.setText('视角23')
            self.push4.setText('视角24')
            self.push5.setText('视角25')
            self.push6.setText('视角26')
            self.push7.setText('视角27')
            self.push8.setText('视角28')
            self.push9.setText('视角29')

    def paintEvent(self, a0: QtGui.QPaintEvent):
        if not self.video_display:
            self.first_frame = True
        else:
            if self.first_frame:
                ret, frame = self.video_display.read()
                global frame_copy
                frame_copy = frame
                self.showPic(frame)
                self.first_frame = False

            if self.track_flag:
                ret, frame = self.video_display.read()
                frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                outputs = self.tracker.track(frame)
                self.pred_bbox = outputs['bbox']
                self.frame_count = outputs['count']
                self.clearRect()
                print('pred_boxo', self.pred_bbox, self.frame_count)
                frame = cv2.rectangle(frame, (int(self.pred_bbox[0]), int(self.pred_bbox[1])),
                                      (int(self.pred_bbox[0] + self.pred_bbox[2]),
                                       int(self.pred_bbox[1] + self.pred_bbox[3])), (0, 255, 255),
                                      3)
                self.Qframe = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3,
                                     QImage.Format_RGB888)
                self.play_label.setPixmap(QPixmap.fromImage(self.Qframe))

                self.update()

            if self.video_change_flag:
                ret, frame = self.video_display.read()
                frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
                self.video_display.set(1, self.frame_count)
                self.video_change_flag = False
                print('old_view : ', self.save_view_2[0], 'new_view : ', self.save_view_2[1])
                new_view, img_local, x_start, y_start = kuashidian.dsd(self.pred_bbox[4], self.pred_bbox[5],
                                                                       self.save_view_2[0],
                                                                       self.save_view_2[1], frame)
                print(' ', self.pred_bbox[4], self.pred_bbox[5])
                img_local = cv2.resize(img_local, (351, 211), interpolation=cv2.INTER_AREA)
                img_local = cv2.cvtColor(img_local, cv2.COLOR_BGR2RGB)
                self.Qframe_ksd = QImage(img_local.data, img_local.shape[1], img_local.shape[0], img_local.shape[1] * 3,
                                         QImage.Format_RGB888)
                self.ksd_view.setPixmap(QPixmap.fromImage(self.Qframe_ksd))
                print('done')
                self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Video_Dis()
    myWin.show()
    sys.exit(app.exec_())
