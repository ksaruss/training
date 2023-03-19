# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_edit_muscle.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QPushButton,
                               QSizePolicy, QWidget)


class Ui_MainAddEditMuscle(object):
    def __init__(self):
        self.label = None
        self.label_2 = None
        self.listWidget = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.pushButton = None
        self.lineEdit = None
        self.gridLayout = None

    def setupUi(self, MainAddEditMuscle):
        if not MainAddEditMuscle.objectName():
            MainAddEditMuscle.setObjectName(u"MainAddEditMuscle")
        MainAddEditMuscle.resize(364, 283)
        self.gridLayout = QGridLayout(MainAddEditMuscle)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(MainAddEditMuscle)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)

        self.pushButton = QPushButton(MainAddEditMuscle)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(MainAddEditMuscle)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 2)

        self.pushButton_3 = QPushButton(MainAddEditMuscle)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.listWidget = QListWidget(MainAddEditMuscle)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2)

        self.label_2 = QLabel(MainAddEditMuscle)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QLabel(MainAddEditMuscle)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.retranslateUi(MainAddEditMuscle)

        QMetaObject.connectSlotsByName(MainAddEditMuscle)

    # setupUi

    def retranslateUi(self, MainAddEditMuscle):
        MainAddEditMuscle.setWindowTitle(QCoreApplication.translate("MainAddEditMuscle", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("MainAddEditMuscle", u"add new muscle", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainAddEditMuscle", u"save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainAddEditMuscle", u"delete", None))
        self.label_2.setText(QCoreApplication.translate("MainAddEditMuscle", u"List muscle group", None))
        self.label.setText(QCoreApplication.translate("MainAddEditMuscle", u"Name", None))

    # retranslateUi
