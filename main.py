import numpy as np
import dataBase
import pandas as pd
import import_from_excel
import queries_in_database


dataBase.create_database()

list_muscle = [{'name_muscle': 'Бицепс'}, {'name_muscle': 'Трицепс'}, {'name_muscle': 'Ноги'}, {'name_muscle': 'Плечи'},
               {'name_muscle': 'Спина'}, {'name_muscle': 'Грудные'}, {'name_muscle': 'Пресс'}]


dataBase.add_new_muscle_in_database(list_muscle)

dataBase.add_new_exercise_in_database({'name_exercise': 'Подъем т-грифа на бицепс',
                                       'muscle_target': 'Бицепс'})
dataBase.add_new_exercise_in_database({'name_exercise': 'Подъем корпуса лежа',
                                       'muscle_target': 'Пресс'})
dataBase.add_new_exercise_in_database({'name_exercise': 'Отжимания от пола',
                                       'muscle_target': 'Грудные'})
dataBase.add_new_exercise_in_database({'name_exercise': 'Французcкий жим стоя',
                                       'muscle_target': 'Трицепс'})
dataBase.add_new_exercise_in_database({'name_exercise': 'Тяга к подбородку',
                                       'muscle_target': 'Плечи'})
dataBase.add_new_exercise_in_database({'name_exercise': 'Присед',
                                       'muscle_target': 'Ноги'})
dataBase.add_new_exercise_in_database({'name_exercise': 'Армейский жим',
                                       'muscle_target': 'Плечи'})

import_from_excel.import_from_excel()

f = dataBase.Training.select(dataBase.Training.week,
                             dataBase.Training.weight,
                             dataBase.Training.repeat,
                             dataBase.Training.exercise,
                             dataBase.Exercise.muscle_target).join(dataBase.Exercise)




f = pd.DataFrame(list(f.dicts()))
# print(f)
f['kg'] = f['repeat'] * f['weight']
table = pd.pivot_table(f, index=['week', 'muscle_target'], aggfunc={'repeat': [np.sum, np.mean],
                                                                    'weight': np.sum,
                                                                    'kg': np.sum})
# print(table)
table['mean_weight'] = table[('kg', 'sum')] / table[('repeat', 'sum')]
table.drop(columns='weight', inplace=True)

print('Плечи', table.xs('Плечи', level=1))
print('Бицепс', table.xs('Бицепс', level=1))
print('Трицепс', table.xs('Трицепс', level=1))
print('Пресс', table.xs('Пресс', level=1))


# print(pd.pivot_table(f, index='week', aggfunc={'kg': np.sum, 'repeat': np.sum}))

# f = dataBase.Training.select()
#
# frame = pd.DataFrame(list(f.dicts()))
# print()