# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_dispalyHgcGbx.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1369, 602)
        icon = QIcon()
        icon.addFile(u"C:/Users/ZHIYU.y/.designer/backup/resource/tubiao.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.990000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.video_display = QLabel(self.centralwidget)
        self.video_display.setObjectName(u"video_display")
        self.video_display.setGeometry(QRect(10, 0, 121, 31))
        self.video_display.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 480, 111, 41))
        self.pushButton.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"background:rgb(255, 255, 255, 60);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.play_label = QLabel(self.centralwidget)
        self.play_label.setObjectName(u"play_label")
        self.play_label.setGeometry(QRect(320, 30, 640, 480))
        self.play_label.setStyleSheet(u"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #6633FF;\n"
"")
        self.play_label.setFrameShape(QFrame.Box)
        self.play_label.setFrameShadow(QFrame.Raised)
        self.play_label.setLineWidth(3)
        self.play_label.setMidLineWidth(0)
        self.play_label.setScaledContents(False)
        self.play_label.setAlignment(Qt.AlignCenter)
        self.play_label.setMargin(0)
        self.select_player = QPushButton(self.centralwidget)
        self.select_player.setObjectName(u"select_player")
        self.select_player.setGeometry(QRect(80, 380, 111, 41))
        self.select_player.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"background:rgb(255, 255, 255, 60);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(80, 430, 111, 41))
        self.start.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"background:rgb(255, 255, 255, 60);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 70, 131, 31))
        self.comboBox.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"background:rgb(255, 255, 255, 60);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 120, 131, 196))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.push0 = QPushButton(self.formLayoutWidget)
        self.push0.setObjectName(u"push0")
        self.push0.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.push0)

        self.push2 = QPushButton(self.formLayoutWidget)
        self.push2.setObjectName(u"push2")
        self.push2.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.push2)

        self.push1 = QPushButton(self.formLayoutWidget)
        self.push1.setObjectName(u"push1")
        self.push1.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.push1)

        self.push6 = QPushButton(self.formLayoutWidget)
        self.push6.setObjectName(u"push6")
        self.push6.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.push6)

        self.push7 = QPushButton(self.formLayoutWidget)
        self.push7.setObjectName(u"push7")
        self.push7.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.push7)

        self.push3 = QPushButton(self.formLayoutWidget)
        self.push3.setObjectName(u"push3")
        self.push3.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.push3)

        self.push8 = QPushButton(self.formLayoutWidget)
        self.push8.setObjectName(u"push8")
        self.push8.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.push8)

        self.push4 = QPushButton(self.formLayoutWidget)
        self.push4.setObjectName(u"push4")
        self.push4.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.push4)

        self.push9 = QPushButton(self.formLayoutWidget)
        self.push9.setObjectName(u"push9")
        self.push9.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.push9)

        self.push5 = QPushButton(self.formLayoutWidget)
        self.push5.setObjectName(u"push5")
        self.push5.setStyleSheet(u"        border-style: outset;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;\n"
"        border-color: beige;\n"
"        font: bold 14px;\n"
"        padding: 6px")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.push5)

        self.ksd_view = QLabel(self.centralwidget)
        self.ksd_view.setObjectName(u"ksd_view")
        self.ksd_view.setGeometry(QRect(990, 60, 351, 211))
        self.ksd_view.setStyleSheet(u"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #6633FF;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1000, 30, 91, 16))
        self.label.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(990, 300, 121, 16))
        self.label_2.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"")
        self.current_player = QLabel(self.centralwidget)
        self.current_player.setObjectName(u"current_player")
        self.current_player.setGeometry(QRect(1100, 330, 121, 161))
        self.current_player.setStyleSheet(u"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #6633FF;\n"
"")
        self.open_video = QPushButton(self.centralwidget)
        self.open_video.setObjectName(u"open_video")
        self.open_video.setGeometry(QRect(80, 330, 111, 41))
        self.open_video.setStyleSheet(u"color:Black;\n"
"font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"background:rgb(255, 255, 255, 60);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1369, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.video_display.setText(QCoreApplication.translate("MainWindow", u"\u5c55\u793a\u7cfb\u7edf", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8ddf\u8e2a", None))
        self.play_label.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u64ad\u653e\u533a\u57df", None))
        self.select_player.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7403\u5458", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u8ddf\u8e2a\u5668\u521d\u59cb\u5316", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"    \u89c6\u89d2  0 - 9", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"    \u89c6\u89d210 - 19", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"    \u89c6\u89d220 - 30", None))

        self.push0.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d20", None))
        self.push2.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d22", None))
        self.push1.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d21", None))
        self.push6.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d26", None))
        self.push7.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d27", None))
        self.push3.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d23", None))
        self.push8.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d28", None))
        self.push4.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d24", None))
        self.push9.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d29", None))
        self.push5.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89d25", None))
        self.ksd_view.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"local frame", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"current player", None))
        self.current_player.setText("")
        self.open_video.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u89c6\u9891\u6587\u4ef6", None))
    # retranslateUi

