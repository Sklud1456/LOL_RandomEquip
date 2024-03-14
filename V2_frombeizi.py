# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
import random
# from widget.UIDetect import UIDetect
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
from PyQt5.QtWidgets import QLabel
import numpy as np

ConflictEquip=[{"贪欲九头蛇","巨型九头蛇","亵渎九头蛇","挺进破坏者"},
                {"大天使之杖","魔宗","末日寒冬"},
                {"蜕生","虚空之杖"},
                {"玛莫提乌斯之噬","斯特拉克的挑战护手","不朽盾弓","大天使之杖"},
                {"多米尼克领主的致意","凡性的提醒","界弓","黑色切割者","赛瑞尔达的怨恨"},
                {"纳沃利迅刃","无尽之刃"},
                {"日炎圣盾","璀璨回响"}]

def cv_read(file_path):
    cv_img = cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    image_rgb = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
    img=cv.resize(image_rgb,(300,300))
    # cv.imshow("Image", cv_img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    return img

class DLabel(QLabel):
    x0 = 0  # 矩形起始点
    y0 = 0
    x1 = 762
    y1 = 633

    sX = 0  # 拖拽操作起始点
    sY = 0
    eX = 0
    eY = 0
    begin = None
    end = None
    open_mouse_flag = False
    select_roi_flag = False
    draw_roi_flag = False
    mode = -1  # -1表示初始状态， 0表示显示状态，1表示框选状态，2表示检测状态,3表示测试状态
    # signal = 0  # 0表示关闭，1表示开启
    listen_mode=0

    # 按下鼠标
    def mousePressEvent(self, event):

        if self.mode == 1:
            self.select_roi_flag = True
            self.x0 = event.x()
            self.y0 = event.y()
            self.x1 = event.x()
            self.y1 = event.y()

            self.sX = event.x()
            self.sY = event.y()
            self.eX = event.x()
            self.eY = event.y()


    # 释放鼠标
    def mouseReleaseEvent(self, event):
        if self.mode == 1:
            self.select_roi_flag = False
            eX = event.x()
            eY = event.y()
            self.setXY(self.sX, self.sY, eX, eY)
            # print('1', eX, eY)
            print('0', self.x0, self.y0)
            print('1', self.x1, self.y1)

    # 移动鼠标
    def mouseMoveEvent(self, event):
        if self.mode == 1:
            if self.select_roi_flag is True:
                eX = event.x()
                eY = event.y()
                self.setXY(self.sX, self.sY, eX, eY)
                if self.draw_roi_flag is True:
                    self.update()

    def reSetXY1(self):
        self.x0 = 0
        self.y0 = 0
        self.x1 = self.width() - 1
        self.y1 = self.height() - 1

    def setXY(self, x0, y0, x1, y1):
        self.x0 = min(x0, x1) if min(x0, x1) > 0 else 0
        self.x1 = max(x0, x1) if max(x0, x1) < self.width() - 1 else self.width() - 1
        self.y0 = min(y0, y1) if min(y0, y1) > 0 else 0
        self.y1 = max(y0, y1) if max(y0, y1) < self.height() - 1 else self.height() - 1



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("Dialog")
        self.resize(800, 500)

        file_path = "装备目录.txt"  # 替换为你的文本文件路径
        self.EquipList = []
        # 打开文本文件，并以只读模式读取内容
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # 处理每一行的内容
                self.EquipList.append(line.strip())

        self.frame_1 = QtWidgets.QLabel(self)
        self.frame_1.setGeometry(QtCore.QRect(50, 30, 38, 16))
        self.frame_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_1.setFixedSize(150, 150)
        self.frame_1.setObjectName("frame_1")

        self.frame_2 = QtWidgets.QLabel(self)
        self.frame_2.setGeometry(QtCore.QRect(300, 30, 38, 16))
        self.frame_2.setFixedSize(150, 150)
        self.frame_2.setObjectName("frame_2")

        self.frame_3 = QtWidgets.QLabel(self)
        self.frame_3.setGeometry(QtCore.QRect(550, 30, 38, 16))
        self.frame_3.setFixedSize(150, 150)
        self.frame_3.setObjectName("frame_3")

        self.frame_4 = QtWidgets.QLabel(self)
        self.frame_4.setGeometry(QtCore.QRect(175, 300, 38, 16))
        self.frame_4.setFixedSize(150, 150)
        self.frame_4.setObjectName("frame_4")

        # self.frame_5 = QtWidgets.QLabel(self)
        # self.frame_5.setGeometry(QtCore.QRect(425, 250, 38, 16))
        # self.frame_5.setBaseSize(QtCore.QSize(200, 200))
        # self.frame_5.setFixedSize(150, 150)
        # self.frame_5.setObjectName("frame_5")

        self.Equip_1 = QtWidgets.QLabel(self)
        self.Equip_1.setGeometry(QtCore.QRect(25, 180, 38, 16))
        self.Equip_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Equip_1.setMinimumSize(200, 50)  # 设置最小尺寸
        self.Equip_1.setMaximumSize(400, 100)  # 设置最大尺寸
        self.Equip_1.setObjectName("Equip_1")

        self.Equip_2 = QtWidgets.QLabel(self)
        self.Equip_2.setGeometry(QtCore.QRect(275, 180, 38, 16))
        self.Equip_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Equip_2.setMinimumSize(200, 50)  # 设置最小尺寸
        self.Equip_2.setMaximumSize(400, 100)  # 设置最大尺寸
        self.Equip_2.setObjectName("Equip_2")


        self.Equip_3 = QtWidgets.QLabel(self)
        self.Equip_3.setGeometry(QtCore.QRect(525, 180, 38, 16))
        self.Equip_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Equip_3.setMinimumSize(200, 50)  # 设置最小尺寸
        self.Equip_3.setMaximumSize(400, 100)  # 设置最大尺寸
        self.Equip_3.setObjectName("Equip_3")



        self.Equip_4 = QtWidgets.QLabel(self)
        self.Equip_4.setGeometry(QtCore.QRect(150, 450, 38, 16))
        self.Equip_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Equip_4.setMinimumSize(200, 50)  # 设置最小尺寸
        self.Equip_4.setMaximumSize(400, 100)  # 设置最大尺寸
        self.Equip_4.setObjectName("Equip_4")

        # self.Equip_5 = QtWidgets.QLabel(self)
        # self.Equip_5.setGeometry(QtCore.QRect(410, 400, 38, 16))
        # self.Equip_5.setAlignment(QtCore.Qt.AlignCenter)
        # self.Equip_5.setMinimumSize(200, 50)  # 设置最小尺寸
        # self.Equip_5.setMaximumSize(400, 100)  # 设置最大尺寸
        # self.Equip_5.setObjectName("Equip_5")

        self.pushButton = QtWidgets.QPushButton(self, )
        self.pushButton.setGeometry(QtCore.QRect(450, 350, 111, 51))
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generate_equip)

        self.pushButton_1 = QtWidgets.QPushButton(self, )
        self.pushButton_1.setGeometry(QtCore.QRect(90, 225, 111, 51))
        self.pushButton_1.setFixedSize(75, 45)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda: self.ramdom_one(1))

        self.pushButton_2 = QtWidgets.QPushButton(self, )
        self.pushButton_2.setGeometry(QtCore.QRect(340, 225, 111, 51))
        self.pushButton_2.setFixedSize(75, 45)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.ramdom_one(2))

        self.pushButton_3 = QtWidgets.QPushButton(self, )
        self.pushButton_3.setGeometry(QtCore.QRect(590, 225, 111, 51))
        self.pushButton_3.setFixedSize(75, 45)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.ramdom_one(3))

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "随机出装生成器"))
        self.pushButton.setText(_translate("Dialog", "随机生成！"))
        self.pushButton_1.setText(_translate("Dialog", "重随"))
        self.pushButton_2.setText(_translate("Dialog", "重随"))
        self.pushButton_3.setText(_translate("Dialog", "重随"))
        # self.Equip_5.setText(_translate("Dialog", "装备5"))
        self.Equip_4.setText(_translate("Dialog", "装备4"))
        self.Equip_3.setText(_translate("Dialog", "装备3"))
        self.Equip_2.setText(_translate("Dialog", "装备2"))
        self.Equip_1.setText(_translate("Dialog", "装备1"))


    def GenerateEquipList(self):
        while(True):
            flag=0
            random_selection = random.sample(self.EquipList, 4)
            random_set=set(random_selection)
            for equipset in ConflictEquip:
                if len(equipset.intersection(random_set))>1:
                    flag=1
                    break
            if flag==0:
                break
        return random_selection

    def generate_equip(self):
        Text=self.GenerateEquipList()
        number=len(Text)
        for i in range(number):
            variable_name = 'Equip_' + str(i+1)
            label = getattr(self, variable_name)
            label.setText(Text[i])

        for i in range(number):
            variable_name = 'frame_' + str(i + 1)
            label = getattr(self, variable_name)
            try:
                picture = cv_read("./EquipIco/{}.png".format(Text[i]))
                img = QtGui.QImage(picture.data, picture.shape[1], picture.shape[0], QtGui.QImage.Format_RGB888)
                label.setPixmap(QtGui.QPixmap.fromImage(img))
                label.setScaledContents(True)
            except Exception as e:
                try:
                    picture = cv_read("./EquipIco/{}.jpg".format(Text[i]))
                    img = QtGui.QImage(picture.data, picture.shape[1], picture.shape[0], QtGui.QImage.Format_RGB888)
                    label.setPixmap(QtGui.QPixmap.fromImage(img))
                    label.setScaledContents(True)
                except Exception as e:
                    print(e)
                    picture = cv_read("./EquipIco/asuka.png")
                    img = QtGui.QImage(picture.data, picture.shape[1], picture.shape[0], QtGui.QImage.Format_RGB888)
                    label.setPixmap(QtGui.QPixmap.fromImage(img))
                    label.setScaledContents(True)

    def ramdom_one(self,n):
        other={self.Equip_1.text(),self.Equip_2.text(),self.Equip_3.text(),self.Equip_4.text()}
        while(True):
            flag=0
            random_one = random.sample(self.EquipList, 1)[0]
            if random_one in other:
                continue
            else:
                templabel = getattr(self, 'Equip_' + str(n))
                orginone=templabel.text()
                tempother=other.copy()
                tempother.remove(orginone)
                tempother.add(random_one)
                for equipset in ConflictEquip:
                    if len(equipset.intersection(tempother)) > 1:
                        flag = 1
                        break
                if flag==0:
                    break


        variable_name = 'Equip_' + str(n)
        label = getattr(self, variable_name)
        label.setText(random_one)


        variable_name = 'frame_' + str(n)
        label = getattr(self, variable_name)
        try:
            picture = cv_read("./EquipIco/{}.png".format(random_one))
            img = QtGui.QImage(picture.data, picture.shape[1], picture.shape[0], QtGui.QImage.Format_RGB888)
            label.setPixmap(QtGui.QPixmap.fromImage(img))
            label.setScaledContents(True)
        except Exception as e:
            try:
                picture = cv_read("./EquipIco/{}.jpg".format(random_one))
                img = QtGui.QImage(picture.data, picture.shape[1], picture.shape[0], QtGui.QImage.Format_RGB888)
                label.setPixmap(QtGui.QPixmap.fromImage(img))
                label.setScaledContents(True)
            except Exception as e:
                print(e)
                picture = cv_read("./EquipIco/asuka.png")
                img = QtGui.QImage(picture.data, picture.shape[1], picture.shape[0], QtGui.QImage.Format_RGB888)
                label.setPixmap(QtGui.QPixmap.fromImage(img))
                label.setScaledContents(True)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # ui = UIDetect()  # 一定要分开写
    # ui.setupUi(mainWin)
    window.show()
    sys.exit(app.exec_())