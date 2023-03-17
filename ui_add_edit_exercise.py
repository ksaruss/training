# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_edit_exercise.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
                               QGridLayout, QLabel, QLineEdit, QListWidget,
                               QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
                               QWidget)


class Ui_MainAddEditExercise(object):
    def setupUi(self, MainAddEditExercise):
        if not MainAddEditExercise.objectName():
            MainAddEditExercise.setObjectName(u"MainAddEditExercise")
        MainAddEditExercise.resize(436, 284)
        self.gridLayout = QGridLayout(MainAddEditExercise)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(MainAddEditExercise)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)

        self.comboBox = QComboBox(MainAddEditExercise)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.comboBox, 3, 4, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(MainAddEditExercise)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(50, 0))
        self.doubleSpinBox.setMaximumSize(QSize(50, 16777215))
        self.doubleSpinBox.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox, 5, 4, 1, 1)

        self.pushButton_3 = QPushButton(MainAddEditExercise)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 0))
        self.pushButton_3.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.pushButton_3, 8, 4, 1, 1)

        self.spinBox = QSpinBox(MainAddEditExercise)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(50, 0))
        self.spinBox.setMaximumSize(QSize(50, 16777215))
        self.spinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.spinBox, 4, 4, 1, 1)

        self.spinBox_2 = QSpinBox(MainAddEditExercise)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(50, 0))
        self.spinBox_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.spinBox_2, 2, 4, 1, 1)

        self.label_2 = QLabel(MainAddEditExercise)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.listWidget = QListWidget(MainAddEditExercise)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.listWidget, 1, 0, 7, 2)

        self.pushButton_2 = QPushButton(MainAddEditExercise)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.pushButton_2, 8, 1, 1, 2)

        self.pushButton = QPushButton(MainAddEditExercise)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)

        self.pushButton_4 = QPushButton(MainAddEditExercise)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 0))
        self.pushButton_4.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.pushButton_4, 8, 3, 1, 1)

        self.label = QLabel(MainAddEditExercise)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)

        self.label_6 = QLabel(MainAddEditExercise)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)

        self.label_3 = QLabel(MainAddEditExercise)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)

        self.label_4 = QLabel(MainAddEditExercise)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)

        self.label_5 = QLabel(MainAddEditExercise)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 1)

        self.retranslateUi(MainAddEditExercise)

        QMetaObject.connectSlotsByName(MainAddEditExercise)

    # setupUi

    def retranslateUi(self, MainAddEditExercise):
        MainAddEditExercise.setWindowTitle(QCoreApplication.translate("MainAddEditExercise", u"Dialog", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainAddEditExercise", u"delete", None))
        self.label_2.setText(QCoreApplication.translate("MainAddEditExercise", u"List exercise", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainAddEditExercise", u"add/edit new coeff", None))
        self.pushButton.setText(QCoreApplication.translate("MainAddEditExercise", u"add new exercise", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainAddEditExercise", u"save", None))
        self.label.setText(QCoreApplication.translate("MainAddEditExercise", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("MainAddEditExercise", u"Week", None))
        self.label_3.setText(QCoreApplication.translate("MainAddEditExercise", u"Target muscle", None))
        self.label_4.setText(QCoreApplication.translate("MainAddEditExercise", u"Base weight", None))
        self.label_5.setText(QCoreApplication.translate("MainAddEditExercise", u"Coeff weight", None))
    # retranslateUi
