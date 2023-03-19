from peewee import *

db = SqliteDatabase('database.db', pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Muscle(BaseModel):
    name_muscle = CharField(primary_key=True)


class Exercise(BaseModel):
    name_exercise = CharField(primary_key=True)
    muscle_target = ForeignKeyField(Muscle, to_field='name_muscle')


class Exercise_coeff(BaseModel):
    name_exercise = ForeignKeyField(Exercise, to_field='name_exercise')
    week = IntegerField(default=1)
    base_weight = IntegerField(default=0)
    coeff_weight = FloatField(default=1)

    class Meta:
        primary_key = CompositeKey('name_exercise', 'week')


class Training(BaseModel):
    id = IntegerField(primary_key=True)
    week = IntegerField()
    date = DateTimeField()
    exercise = ForeignKeyField(Exercise, to_field='name_exercise')
    weight = FloatField()
    repeat = IntegerField()
    number = IntegerField()
    recreation = IntegerField()
    type_ = CharField()


class CalcMaxWeightOneRepeat(BaseModel):
    week = IntegerField()
    exercise = ForeignKeyField(Exercise, to_field='name_exercise')
    type_ = CharField()
    test_weight = FloatField(null=True)
    repeat = IntegerField(null=True)
    calc_max_weight_one_repeat = FloatField()


def create_database() -> None:
    db.create_tables([Muscle, Exercise, Exercise_coeff, Training, CalcMaxWeightOneRepeat])


def add_new_muscle_in_database(data: dict | list[dict]) -> None:
    if isinstance(data, dict):
        data = [data]
    for muscle in data:
        try:
            new_row = Muscle.create(name_muscle=muscle['name_muscle'])
            print(f'Группа мышц "{muscle["name_muscle"]}" добавлена в базу')
        except IntegrityError:
            print(f'Группа мышц "{muscle["name_muscle"]}" уже есть в базе')


def add_new_exercise_in_database(data: dict) -> None:
    try:
        new_row = Exercise.create(name_exercise=data['name_exercise'], muscle_target=data['muscle_target'])
        print(f'Упражнение "{data["name_exercise"]}" добавлено в базу')
        new_row_coeff = Exercise_coeff.create(**data)
    except IntegrityError:
        print(f'Упражнение "{data["name_exercise"]}" уже есть в базе')


def add_new_exercise_coeff_in_database(data: dict) -> None:
    try:
        new_row = Exercise_coeff.create(**data)
    except IntegrityError:
        print('fffff')


def add_new_training_in_database(data: dict | list[dict]) -> None:
    print(Training.insert_many(data).on_conflict_ignore().execute())


def add_new_calc_max_weight_one_repeat(data: dict) -> None:
    new_row = CalcMaxWeightOneRepeat.create(**data)