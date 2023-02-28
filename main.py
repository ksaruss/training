import numpy as np
import dataBase
import pandas as pd
import import_from_excel

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
# dataBase.add_new_exercise({'name_exercise': 'Французский жим стоя',
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

# f = pd.DataFrame(list(f.dicts()))
# print(f)
# table = pd.pivot_table(f, index=['week', 'muscle_target'], aggfunc={'repeat': np.sum,
#                                                                     'weight': np.mean})
# table['ton'] = table['repeat'] * table['weight']
# print(table)


# import_from_excel.import_from_excel()

f = dataBase.Training.select()
t = dataBase.Exercise.select()
print(list(t.dicts()))
print(pd.DataFrame(list(f.dicts()))['exercise'])