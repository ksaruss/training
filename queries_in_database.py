from dataBase import *


def get_muscle(not_muscle: list[str] = None):
    if not_muscle is None:
        not_muscle = []
    q = Muscle.select().where(Muscle.name_muscle.not_in(not_muscle))
    # for i in q:
    #     print(i)
    return list(q)


def get_exercise(not_exercise: list[str] = None):
    if not_exercise is None:
        not_exercise = []
    q = Exercise.select().where(Exercise.name_exercise.not_in(not_exercise))
    # for i in q.dicts():
    #     print(i)
    return list(q)


def get_exercise2(exercise: str):
    q = Exercise.select(Exercise_coeff,
                        Exercise.muscle_target).where(Exercise.name_exercise == exercise)\
        .join(Exercise_coeff, on=(Exercise.name_exercise == Exercise_coeff.name_exercise))
    return list(q.dicts())

def get_training(training_week_start: int = 1, training_week_stop: int = 1000):
    q = Training.select().where(Training.week.between(training_week_start, training_week_stop))
    # for i in q.dicts():
    #     print(i)
    return list(q)


def get_qu(s, e, t1, t2):
    mus = get_muscle(s)
    ex = get_exercise(e)
    tr = get_training(t1, t2)

    q = Muscle.select(Muscle.name_muscle,
                      Exercise.name_exercise,
                      Training.id,
                      Training.week,
                      Training.weight,
                      Training.repeat,
                      Exercise_coeff.week,
                      Exercise_coeff.base_weight,
                      Exercise_coeff.coeff_weight.alias('cw'),
                      CalcMaxWeightOneRepeat.calc_max_weight_one_repeat,
                      CalcMaxWeightOneRepeat.week.alias('week_coe1')) \
        .where(Muscle.name_muscle.in_(mus)) \
        .join(Exercise, on=((Exercise.name_exercise.in_(ex))
                           & (Muscle.name_muscle == Exercise.muscle_target))) \
        .join(Training, on=((Training.id.in_(tr))
                            & (Training.exercise == Exercise.name_exercise))) \
        .join(Exercise_coeff, on=(Exercise_coeff.name_exercise == Exercise.name_exercise)) \
        .join(CalcMaxWeightOneRepeat, JOIN.LEFT_OUTER, on=((CalcMaxWeightOneRepeat.exercise == Training.exercise)
                                                           & CalcMaxWeightOneRepeat.week == Training.week))

    for i in q.dicts():
        print(i)
    print(len(list(q)))
