import pandas as pd
from dataBase import add_new_training


def import_from_excel():
    f = pd.read_excel('тренировка.xlsx', sheet_name='Лист3')
    f.rename(columns={'№': 'id', 'Неделя': 'week', 'Упражнение': 'exercise',
                      'Дата': 'date', 'Вес': 'weight', 'Повт.': 'repeat',
                      'Отдых': 'recreation', '№ подхода': 'number', 'Тип подхода': 'type_'}, inplace=True)

    # print(f.rename(columns={'Упражнение': 'ntrtgij'}))

    f['date'] = f['date'].apply(lambda x: x.date())

    print(f.to_dict(orient='records'))
    l = f.to_dict(orient='records')
    add_new_training(l)

