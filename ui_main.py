# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 600)
        self.action_Add_Edit_new_group_mucsle = QAction(MainWindow)
        self.action_Add_Edit_new_group_mucsle.setObjectName(u"action_Add_Edit_new_group_mucsle")
        self.action_Add_Edit_new_exercise = QAction(MainWindow)
        self.action_Add_Edit_new_exercise.setObjectName(u"action_Add_Edit_new_exercise")
        self.action_Add_Edit_new_traning = QAction(MainWindow)
        self.action_Add_Edit_new_traning.setObjectName(u"action_Add_Edit_new_traning")
        self.action_Import_traning_from_excel = QAction(MainWindow)
        self.action_Import_traning_from_excel.setObjectName(u"action_Import_traning_from_excel")
        self.action_Add_Edit_weight_coeff = QAction(MainWindow)
        self.action_Add_Edit_weight_coeff.setObjectName(u"action_Add_Edit_weight_coeff")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 476, 21))
        self.menu_Add_Edit = QMenu(self.menubar)
        self.menu_Add_Edit.setObjectName(u"menu_Add_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Add_Edit.menuAction())
        self.menu_Add_Edit.addAction(self.action_Add_Edit_new_group_mucsle)
        self.menu_Add_Edit.addAction(self.action_Add_Edit_new_exercise)
        self.menu_Add_Edit.addAction(self.action_Add_Edit_new_traning)
        self.menu_Add_Edit.addAction(self.action_Import_traning_from_excel)
        self.menu_Add_Edit.addAction(self.action_Add_Edit_weight_coeff)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Add_Edit_new_group_mucsle.setText(
            QCoreApplication.translate("MainWindow", u"&Add/Edit new group mucsle", None))
        self.action_Add_Edit_new_exercise.setText(
            QCoreApplication.translate("MainWindow", u"&Add/Edit new exercise", None))
        self.action_Add_Edit_new_traning.setText(
            QCoreApplication.translate("MainWindow", u"&Add/Edit new traning", None))
        self.action_Import_traning_from_excel.setText(
            QCoreApplication.translate("MainWindow", u"&Import traning from excel", None))
        self.action_Add_Edit_weight_coeff.setText(
            QCoreApplication.translate("MainWindow", u"&Add/Edit weight coeff", None))
        self.menu_Add_Edit.setTitle(QCoreApplication.translate("MainWindow", u"&Add/Edit", None))
    # retranslateUi
