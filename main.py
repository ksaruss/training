import sys

import numpy as np
import dataBase
import pandas as pd
import import_from_excel

from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.gg()
        self.ui.listWidget.clicked.connect(self.hdfud)
        self.ui.action_add_edit.triggered.connect(self.gg)

    def start(self):
        print('pass')

    def hdfud(self):
        print(self.ui.listWidget.currentIndex())

    def gg(self):
        q = dataBase.Muscle.select()
        for i in q:
            self.ui.listWidget.addItem(str(i))

app = QApplication()
windows = MainWindows()
windows.show()
sys.exit(app.exec())

# dataBase.create_database()
#
# list_muscle = [{'name_muscle': 'Бицепс'}, {'name_muscle': 'Трицепс'}, {'name_muscle': 'Ноги'}, {'name_muscle': 'Плечи'},
#                {'name_muscle': 'Спина'}, {'name_muscle': 'Грудные'}, {'name_muscle': 'Пресс'}]
#
#
# dataBase.add_new_muscle_in_database(list_muscle)
#
# dataBase.add_new_exercise({'name_exercise': 'Подъем т-грифа на бицепс',
#                            'muscle_target': 'Бицепс'})
# dataBase.add_new_exercise({'name_exercise': 'Подъем корпуса лежа',
#                            'muscle_target': 'Пресс'})
# dataBase.add_new_exercise({'name_exercise': 'Отжимания от пола',
#                            'muscle_target': 'Грудные'})
# dataBase.add_new_exercise({'name_exercise': 'Французcкий жим стоя',
#                            'muscle_target': 'Трицепс'})
# dataBase.add_new_exercise({'name_exercise': 'Тяга к подбородку',
#                            'muscle_target': 'Плечи'})
# dataBase.add_new_exercise({'name_exercise': 'Присед',
#                            'muscle_target': 'Ноги'})
# dataBase.add_new_exercise({'name_exercise': 'Армейский жим',
#                            'muscle_target': 'Плечи'})


# dataBase.add_new_training({'week': 2,
#                            'date': '27.02.2023',
#                            'exercise': 'Французский жим',
#                            'weight': 24,
#                            'repeat': 10,
#                            'recreation': 120,
#                            'type_': 'о'})

#
# f = dataBase.Training.select(dataBase.Training.week,
#                              dataBase.Training.weight,
#                              dataBase.Training.repeat,
#                              dataBase.Training.exercise,
#                              dataBase.Exercise.muscle_target).join(dataBase.Exercise)
#
# import_from_excel.import_from_excel()
#
#
# f = pd.DataFrame(list(f.dicts()))
# # print(f)
# f['kg'] = f['repeat'] * f['weight']
# table = pd.pivot_table(f, index=['week', 'muscle_target'], aggfunc={'repeat': [np.sum, np.mean],
#                                                                     'weight': np.sum,
#                                                                     'kg': np.sum})
# print(table)
# table['mean_weight'] = table[('kg', 'sum')] / table[('repeat', 'sum')]
# table.drop(columns='weight', inplace=True)
#
# print(table.xs('Бицепс', level=1))




# f = dataBase.Training.select()
#
# frame = pd.DataFrame(list(f.dicts()))
# print()