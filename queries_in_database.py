import dataBase

def get_muscle():
    q = dataBase.Muscle.select()
    for i in q:
        print(i)

def get_exercise():
    q = dataBase.Exercise.select()
    for i in q:
        print(i)