import numpy as np
import dataBase
import pandas as pd
import import_from_excel
import queries_in_database
from peewee import *
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_main import Ui_MainWindow
from ui_add_edit_muscle import Ui_MainAddEditMuscle
from ui_add_edit_exercise import Ui_MainAddEditExercise


# dataBase.create_database()
#
# list_muscle = [{'name_muscle': 'Бицепс'}, {'name_muscle': 'Трицепс'}, {'name_muscle': 'Ноги'}, {'name_muscle': 'Плечи'},
#                {'name_muscle': 'Спина'}, {'name_muscle': 'Грудные'}, {'name_muscle': 'Пресс'}]
#
#
# dataBase.add_new_muscle_in_database(list_muscle)
#
# dataBase.add_new_exercise_in_database({'name_exercise': 'Подъем т-грифа на бицепс',
#                                        'muscle_target': 'Бицепс'})
# dataBase.add_new_exercise_in_database({'name_exercise': 'Подъем корпуса лежа',
#                                        'muscle_target': 'Пресс', 'base_weight': 10})
# dataBase.add_new_exercise_in_database({'name_exercise': 'Отжимания от пола',
#                                        'muscle_target': 'Грудные', 'base_weight': 40})
# dataBase.add_new_exercise_in_database({'name_exercise': 'Французcкий жим стоя',
#                                        'muscle_target': 'Трицепс'})
# dataBase.add_new_exercise_in_database({'name_exercise': 'Тяга к подбородку',
#                                        'muscle_target': 'Плечи'})
# dataBase.add_new_exercise_in_database({'name_exercise': 'Присед',
#                                        'muscle_target': 'Ноги'})
# dataBase.add_new_exercise_in_database({'name_exercise': 'Армейский жим',
#                                        'muscle_target': 'Плечи'})
#
# import_from_excel.import_from_excel()

# dataBase.add_new_calc_max_weight_one_repeat({'week': 1, 'exercise': 'Подъем т-грифа на бицепс',
#                                              'type_': 'analytic', 'calc_max_weight_one_repeat': 34.5})
#
# dataBase.add_new_calc_max_weight_one_repeat({'week': 5, 'exercise': 'Подъем т-грифа на бицепс',
#                                              'type_': 'analytic', 'calc_max_weight_one_repeat': 39.5})


# f = dataBase.Training.select(dataBase.Training.week,
#                              dataBase.Training.weight,
#                              dataBase.Training.repeat,
#                              dataBase.Training.exercise,
#                              dataBase.Exercise.muscle_target,
#                              dataBase.Exercise_coeff.base_weight,
#                              dataBase.Exercise_coeff.coeff_weight,
#                              dataBase.CalcMaxWeightOneRepeat.calc_max_weight_one_repeat) \
#     .join(dataBase.Exercise) \
#     .join(dataBase.Exercise_coeff) \
#     .join(dataBase.CalcMaxWeightOneRepeat, JOIN.LEFT_OUTER,
#           on=((dataBase.Training.exercise == dataBase.CalcMaxWeightOneRepeat.exercise))
#              & (dataBase.Training.week == dataBase.CalcMaxWeightOneRepeat.week))
#
# f = pd.DataFrame(list(f.dicts()))
#
# f['calc_max_weight_one_repeat'].fillna(method="ffill", inplace=True)
# print(f.loc[f['muscle_target'] == 'Бицепс'][45:50])
# f['kg'] = f['repeat'] * f['weight']
# f['cor_w'] = (f['weight'] + f['base_weight']) * f['coeff_weight'] * f['repeat']
#
# table = pd.pivot_table(f, index=['week', 'muscle_target'], aggfunc={'repeat': np.sum,
#                                                                     'weight': np.sum,
#                                                                     'kg': np.sum,
#                                                                     'cor_w': np.sum})
#
# table['mean_weight'] = table['kg'] / table['repeat']
# table['mean_weigth_corr'] = table['cor_w'] / table['repeat']
# table.drop(columns='weight', inplace=True)
#
# print('Грудные', table.xs('Грудные', level=1))
# print('Бицепс', table.xs('Бицепс', level=1))
# print('Трицепс', table.xs('Трицепс', level=1))
# print('Пресс', table.xs('Пресс', level=1))
#
# print(pd.pivot_table(f, index='week', aggfunc={'kg': np.sum, 'repeat': np.sum}))


class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Add_Edit_new_group_mucsle.triggered.connect(self.start)

        self.ui.action_Add_Edit_new_exercise.triggered.connect(self.hdfud)

        self.win = Wind()


        self.win2 = Wind2()

    def start(self):
        self.win.show()
        q = dataBase.Muscle.select()
        for i in q:
            self.win.ui.listWidget.addItem(str(i))
        print(self.win.ui.listWidget.currentItem())

    def hdfud(self):
        self.win2.show()

    def gg(self):
        pass


class Wind(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainAddEditMuscle()
        self.ui.setupUi(self)
        self.ui.listWidget.clicked.connect(self.click_listWidget)

    def click_listWidget(self):
        self.ui.lineEdit.setText(self.ui.listWidget.currentItem().text())


class Wind2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainAddEditExercise()
        self.ui.setupUi(self)


app = QApplication()
windows = MainWindows()
windows.show()
sys.exit(app.exec())
