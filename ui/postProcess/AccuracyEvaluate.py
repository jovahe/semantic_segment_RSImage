# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccuracyEvaluate.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_accuracy_evaluate(object):
    def setupUi(self, Dialog_accuracy_evaluate):
        Dialog_accuracy_evaluate.setObjectName("Dialog_accuracy_evaluate")
        Dialog_accuracy_evaluate.resize(416, 218)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_accuracy_evaluate)
        self.buttonBox.setGeometry(QtCore.QRect(190, 180, 211, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog_accuracy_evaluate)
        self.widget.setGeometry(QtCore.QRect(12, 12, 381, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(55, 23))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_gt = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_gt.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_gt.setObjectName("lineEdit_gt")
        self.horizontalLayout_8.addWidget(self.lineEdit_gt)
        self.pushButton_gt = QtWidgets.QPushButton(self.widget)
        self.pushButton_gt.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_gt.setObjectName("pushButton_gt")
        self.horizontalLayout_8.addWidget(self.pushButton_gt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(55, 23))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lineEdit_mask = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_mask.setMinimumSize(QtCore.QSize(201, 23))
        self.lineEdit_mask.setObjectName("lineEdit_mask")
        self.horizontalLayout_9.addWidget(self.lineEdit_mask)
        self.pushButton_mask = QtWidgets.QPushButton(self.widget)
        self.pushButton_mask.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.horizontalLayout_9.addWidget(self.pushButton_mask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_min = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_min.setObjectName("spinBox_min")
        self.horizontalLayout_2.addWidget(self.spinBox_min)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_max = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_max.setMinimum(1)
        self.spinBox_max.setProperty("value", 2)
        self.spinBox_max.setObjectName("spinBox_max")
        self.horizontalLayout_2.addWidget(self.spinBox_max)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_gupid = QtWidgets.QComboBox(self.widget)
        self.comboBox_gupid.setObjectName("comboBox_gupid")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.comboBox_gupid.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_gupid)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.doubleSpinBox_rate = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_rate.setMinimum(0.01)
        self.doubleSpinBox_rate.setMaximum(1.0)
        self.doubleSpinBox_rate.setSingleStep(0.01)
        self.doubleSpinBox_rate.setProperty("value", 0.5)
        self.doubleSpinBox_rate.setObjectName("doubleSpinBox_rate")
        self.horizontalLayout.addWidget(self.doubleSpinBox_rate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog_accuracy_evaluate)
        self.comboBox_gupid.setCurrentIndex(5)
        self.buttonBox.rejected.connect(Dialog_accuracy_evaluate.reject)
        self.buttonBox.accepted.connect(Dialog_accuracy_evaluate.slot_ok)
        self.pushButton_gt.clicked.connect(Dialog_accuracy_evaluate.slot_select_gt_file)
        self.pushButton_mask.clicked.connect(Dialog_accuracy_evaluate.slot_select_mask_file)
        QtCore.QMetaObject.connectSlotsByName(Dialog_accuracy_evaluate)

    def retranslateUi(self, Dialog_accuracy_evaluate):
        _translate = QtCore.QCoreApplication.translate
        Dialog_accuracy_evaluate.setWindowTitle(_translate("Dialog_accuracy_evaluate", "Evaluate accuracy"))
        self.label_6.setText(_translate("Dialog_accuracy_evaluate", "Ground Truth:"))
        self.pushButton_gt.setText(_translate("Dialog_accuracy_evaluate", "Open"))
        self.label_8.setText(_translate("Dialog_accuracy_evaluate", "Predict mask:"))
        self.pushButton_mask.setText(_translate("Dialog_accuracy_evaluate", "Open"))
        self.groupBox.setTitle(_translate("Dialog_accuracy_evaluate", "Values range"))
        self.label.setText(_translate("Dialog_accuracy_evaluate", "min:"))
        self.label_2.setText(_translate("Dialog_accuracy_evaluate", "max:"))
        self.label_4.setText(_translate("Dialog_accuracy_evaluate", "GPU ID:"))
        self.comboBox_gupid.setItemText(0, _translate("Dialog_accuracy_evaluate", "0"))
        self.comboBox_gupid.setItemText(1, _translate("Dialog_accuracy_evaluate", "1"))
        self.comboBox_gupid.setItemText(2, _translate("Dialog_accuracy_evaluate", "2"))
        self.comboBox_gupid.setItemText(3, _translate("Dialog_accuracy_evaluate", "3"))
        self.comboBox_gupid.setItemText(4, _translate("Dialog_accuracy_evaluate", "4"))
        self.comboBox_gupid.setItemText(5, _translate("Dialog_accuracy_evaluate", "5"))
        self.label_3.setText(_translate("Dialog_accuracy_evaluate", "Check rate:"))

