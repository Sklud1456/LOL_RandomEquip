# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UItest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 410)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 350, 111, 51))
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setVerticalSpacing(7)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.Equip_4 = QtWidgets.QLabel(self.layoutWidget)
        self.Equip_4.setObjectName("Equip_4")
        self.gridLayout_1.addWidget(self.Equip_4, 4, 3, 1, 1)
        self.Equip_5 = QtWidgets.QLabel(self.layoutWidget)
        self.Equip_5.setObjectName("Equip_5")
        self.gridLayout_1.addWidget(self.Equip_5, 3, 3, 1, 1)
        self.Equip_3 = QtWidgets.QLabel(self.layoutWidget)
        self.Equip_3.setObjectName("Equip_3")
        self.gridLayout_1.addWidget(self.Equip_3, 2, 3, 1, 1)
        self.Equip_2 = QtWidgets.QLabel(self.layoutWidget)
        self.Equip_2.setObjectName("Equip_2")
        self.gridLayout_1.addWidget(self.Equip_2, 1, 3, 1, 1)
        self.Equip_1 = QtWidgets.QLabel(self.layoutWidget)
        self.Equip_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Equip_1.setObjectName("Equip_1")
        self.gridLayout_1.addWidget(self.Equip_1, 0, 3, 1, 1)
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_1.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_1.addWidget(self.frame_2, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_1.addWidget(self.frame_3, 2, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_1.addWidget(self.frame_4, 3, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_1.addWidget(self.frame_5, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "装备随机生成器"))
        self.pushButton.setText(_translate("Dialog", "随机生成！"))
        self.Equip_4.setText(_translate("Dialog", "装备5"))
        self.Equip_5.setText(_translate("Dialog", "装备4"))
        self.Equip_3.setText(_translate("Dialog", "装备3"))
        self.Equip_2.setText(_translate("Dialog", "装备2"))
        self.Equip_1.setText(_translate("Dialog", "装备1"))
