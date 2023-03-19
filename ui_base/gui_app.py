from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_base.ui_main import Ui_MainWindow
from ui_base.ui_add_edit_muscle import Ui_MainAddEditMuscle
from ui_base.ui_add_edit_exercise import Ui_MainAddEditExercise
import queries_in_database

import sys


class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Add_Edit_new_group_mucsle.triggered.connect(self.open_window_add_edit_new_group_mucsle)

        self.ui.action_Add_Edit_new_exercise.triggered.connect(self.open_window_add_edit_new_exercise)

        self.window_add_edit_muscle = WindowAddEditMuscle()

        self.window_add_edit_exercise = WindowAddEditExercise()

    def open_window_add_edit_new_group_mucsle(self):
        self.window_add_edit_muscle.ui.listWidget.clear()
        self.window_add_edit_muscle.show()
        q = queries_in_database.get_muscle()
        for i in q:
            self.window_add_edit_muscle.ui.listWidget.addItem(str(i))

    def open_window_add_edit_new_exercise(self):
        self.window_add_edit_exercise.ui.listWidget.clear()
        self.window_add_edit_exercise.show()
        self.window_add_edit_exercise.start()


class WindowAddEditMuscle(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainAddEditMuscle()
        self.ui.setupUi(self)
        self.ui.listWidget.clicked.connect(self.click_listWidget)

    def click_listWidget(self):
        self.ui.lineEdit.setText(self.ui.listWidget.currentItem().text())


class WindowAddEditExercise(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainAddEditExercise()
        self.ui.setupUi(self)
        self.ui.listWidget.clicked.connect(self.click_listWidget)

    def start(self):
        q = queries_in_database.get_exercise()
        for i in q:
            print(i.name_exercise)
            self.ui.listWidget.addItem(str(i))
        q = queries_in_database.get_muscle()
        for i in q:
            self.ui.comboBox.addItem(str(i))

    def click_listWidget(self):
        q = queries_in_database.get_exercise2(self.ui.listWidget.currentItem().text())
        q = q[0]
        self.ui.lineEdit.setText(q['name_exercise'])
        self.ui.spinBox.setValue(int(q['base_weight']))
        self.ui.comboBox.setItemText(0, q['muscle_target'])
        self.ui.spinBox_2.setValue(int(q['week']))
        self.ui.doubleSpinBox.setValue(float(q['coeff_weight']))
        print(q)

def start_gui_app():
    app = QApplication()
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())
