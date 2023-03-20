import queries_in_database
from ui_base.gui_app import start_gui_app
import matplotlib.pyplot as plt
import math
import dataBase
import import_from_excel
import pandas as pd
from peewee import *
import numpy as np

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
#                                        'muscle_target': 'Пресс', 'base_weight': 20})
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
#
# dataBase.add_new_calc_max_weight_one_repeat({'week': 1, 'exercise': 'Подъем т-грифа на бицепс',
#                                              'type_': 'analytic', 'calc_max_weight_one_repeat': 34.5})
#
# dataBase.add_new_calc_max_weight_one_repeat({'week': 5, 'exercise': 'Подъем т-грифа на бицепс',
#                                              'type_': 'analytic', 'calc_max_weight_one_repeat': 39.5})

# dataBase.add_new_calc_max_weight_one_repeat({'week': 1, 'exercise': 'Французcкий жим стоя',
#                                              'type_': 'analytic', 'calc_max_weight_one_repeat': 39.5})
# dataBase.add_new_calc_max_weight_one_repeat({'week': 6, 'exercise': 'Французcкий жим стоя',
#                                              'type_': 'analytic', 'calc_max_weight_one_repeat': 42})

f = dataBase.Training.select(dataBase.Training.week,
                             dataBase.Training.weight,
                             dataBase.Training.repeat,
                             dataBase.Training.exercise,
                             dataBase.Exercise.muscle_target,
                             dataBase.Exercise_coeff.base_weight.alias('B_W'),
                             dataBase.Exercise_coeff.coeff_weight.alias('C_W'),
                             dataBase.CalcMaxWeightOneRepeat.calc_max_weight_one_repeat.alias('MWR')) \
    .join(dataBase.Exercise) \
    .join(dataBase.Exercise_coeff) \
    .join(dataBase.CalcMaxWeightOneRepeat, JOIN.LEFT_OUTER,
          on=(dataBase.Training.exercise == dataBase.CalcMaxWeightOneRepeat.exercise)
             & (dataBase.Training.week == dataBase.CalcMaxWeightOneRepeat.week))

f = pd.DataFrame(list(f.dicts()))

l = f['exercise'].unique()

f.set_index(['week'], inplace=True)

new_df = pd.DataFrame()

for i in l:
    f.loc[f['exercise'] == i] = f.loc[f['exercise'] == i].fillna(method='ffill')




print(f.loc[f['muscle_target'] == 'Бицепс'][45:50])
f['kg'] = f['repeat'] * f['weight']
f['cor_w'] = (f['weight'] + f['B_W']) * f['C_W'] * f['repeat']


def calc_inten(df):
    coeff = df['weight'] / df['MWR']
    return round(0.36 + 0.0015 * math.exp((coeff - 0.71) / 0.035) + 0.65 * math.exp((coeff - 0.71) / 0.16), 9)


f['int'] = f.apply(calc_inten, axis=1)

f['int'] = round(f['int'] * f['repeat'] * f['weight'])

table = pd.pivot_table(f, index=['week', 'muscle_target'], aggfunc={'repeat': np.sum,
                                                                    'weight': np.sum,
                                                                    'kg': np.sum,
                                                                    'cor_w': np.sum,
                                                                    'int': np.sum,
                                                                    'MWR': np.mean})

table['mean_weight'] = table['kg'] / table['repeat']
table['mean_weigth_corr'] = table['cor_w'] / table['repeat']
table.drop(columns='weight', inplace=True)

print('Плечи', table.xs('Грудные', level=1))
print('Бицепс', table.xs('Бицепс', level=1))
print('Трицепс', table.xs('Трицепс', level=1))
print('Пресс', table.xs('Пресс', level=1))

# start_gui_app()

# queries_in_database.get_qu(['Пресс', 'Ноги'], ['Отжимания от пола'], 4, 5)


print(table.pivot_table(index='week', aggfunc={'cor_w': np.sum,
                                         'int': np.sum,
                                         }))

