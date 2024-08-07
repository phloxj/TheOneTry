# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdf.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 626)
        icon = QIcon()
        icon.addFile(u"e.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(14, 16, 121, 51))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(14, 221, 111, 41))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(14, 416, 151, 41))
        self.pushButton_pdf2png = QPushButton(Form)
        self.pushButton_pdf2png.setObjectName(u"pushButton_pdf2png")
        self.pushButton_pdf2png.setGeometry(QRect(130, 350, 121, 31))
        self.pushButton_png2pdf = QPushButton(Form)
        self.pushButton_png2pdf.setObjectName(u"pushButton_png2pdf")
        self.pushButton_png2pdf.setGeometry(QRect(130, 160, 121, 31))
        self.pushButton_NameChange = QPushButton(Form)
        self.pushButton_NameChange.setObjectName(u"pushButton_NameChange")
        self.pushButton_NameChange.setGeometry(QRect(130, 544, 121, 31))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(64, 517, 48, 16))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(64, 491, 48, 16))
        self.lineEdit_oldname = QLineEdit(Form)
        self.lineEdit_oldname.setObjectName(u"lineEdit_oldname")
        self.lineEdit_oldname.setGeometry(QRect(213, 491, 61, 20))
        self.lineEdit_newname = QLineEdit(Form)
        self.lineEdit_newname.setObjectName(u"lineEdit_newname")
        self.lineEdit_newname.setGeometry(QRect(213, 517, 61, 20))
        self.lineEdit_choice3 = QLineEdit(Form)
        self.lineEdit_choice3.setObjectName(u"lineEdit_choice3")
        self.lineEdit_choice3.setGeometry(QRect(149, 460, 430, 20))
        self.lineEdit_choice3.setReadOnly(False)
        self.pushButton_choice3 = QPushButton(Form)
        self.pushButton_choice3.setObjectName(u"pushButton_choice3")
        self.pushButton_choice3.setGeometry(QRect(50, 460, 75, 24))
        self.lineEdit_input1 = QLineEdit(Form)
        self.lineEdit_input1.setObjectName(u"lineEdit_input1")
        self.lineEdit_input1.setGeometry(QRect(178, 101, 401, 20))
        self.lineEdit_choice1 = QLineEdit(Form)
        self.lineEdit_choice1.setObjectName(u"lineEdit_choice1")
        self.lineEdit_choice1.setGeometry(QRect(178, 71, 401, 20))
        self.lineEdit_choice1.setReadOnly(False)
        self.pushButton_choice1 = QPushButton(Form)
        self.pushButton_choice1.setObjectName(u"pushButton_choice1")
        self.pushButton_choice1.setGeometry(QRect(64, 71, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(64, 127, 27, 16))
        self.lineEdit_output1 = QLineEdit(Form)
        self.lineEdit_output1.setObjectName(u"lineEdit_output1")
        self.lineEdit_output1.setGeometry(QRect(178, 127, 401, 20))
        self.lineEdit_output1.setReadOnly(False)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(64, 101, 108, 16))
        self.lineEdit_output2 = QLineEdit(Form)
        self.lineEdit_output2.setObjectName(u"lineEdit_output2")
        self.lineEdit_output2.setGeometry(QRect(178, 322, 401, 20))
        self.lineEdit_output2.setReadOnly(False)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(64, 322, 27, 16))
        self.pushButton_choice2 = QPushButton(Form)
        self.pushButton_choice2.setObjectName(u"pushButton_choice2")
        self.pushButton_choice2.setGeometry(QRect(64, 266, 75, 24))
        self.lineEdit_input2 = QLineEdit(Form)
        self.lineEdit_input2.setObjectName(u"lineEdit_input2")
        self.lineEdit_input2.setGeometry(QRect(178, 296, 401, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(64, 296, 108, 16))
        self.lineEdit_choice2 = QLineEdit(Form)
        self.lineEdit_choice2.setObjectName(u"lineEdit_choice2")
        self.lineEdit_choice2.setGeometry(QRect(178, 266, 401, 20))
        self.lineEdit_choice2.setReadOnly(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"For_pdf", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">png2pdf</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">pdf2png</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u6269\u5c55\u540d\u91cd\u547d\u540d</span></p></body></html>", None))
        self.pushButton_pdf2png.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.pushButton_png2pdf.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.pushButton_NameChange.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u65b0\u6269\u5c55\u540d", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u65e7\u6269\u5c55\u540d", None))
        self.lineEdit_oldname.setText(QCoreApplication.translate("Form", u".jpg", None))
        self.lineEdit_newname.setText(QCoreApplication.translate("Form", u".png", None))
        self.lineEdit_choice3.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f60\u9009\u62e9\u7684\u8def\u5f84", None))
        self.pushButton_choice3.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84", None))
        self.lineEdit_input1.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f60\u9009\u62e9\u7684\u6587\u4ef6\u540d", None))
        self.lineEdit_choice1.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f60\u9009\u62e9\u7684\u8def\u5f84", None))
        self.pushButton_choice1.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6587\u4ef6\u540d\uff08\u53ef\u6539\uff09", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa:", None))
        self.pushButton_choice2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84", None))
        self.lineEdit_input2.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f60\u9009\u62e9\u7684\u6587\u4ef6\u540d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6587\u4ef6\u540d\uff08\u53ef\u6539\uff09", None))
        self.lineEdit_choice2.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f60\u9009\u62e9\u7684\u8def\u5f84", None))
    # retranslateUi

