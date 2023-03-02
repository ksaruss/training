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


class CalcMaxRepeat(BaseModel):
    id = AutoField()
    week = IntegerField()
    exercise = ForeignKeyField(Exercise, to_field='id')
    test_weight = FloatField()
    repeat = IntegerField()
    calc_max_repeat = FloatField()


def add_in_database(table: BaseModel, data: dict | list[dict]) -> None:
    table.insert_many(data).on_conflict_replace().execute()


def create_database() -> None:
    db.create_tables([Muscle, Exercise, Training, CalcMaxRepeat])


def add_new_muscle_in_database(data: dict | list[dict]) -> None:
    try:
        Muscle.insert(data).execute()
    except:
        print('Данная группа мышц уже есть в базе')


def add_new_exercise_in_database(data: dict) -> None:
    try:
        Exercise.insert(data).execute()
    except:
        print('Данное упражнение уже есть в базе')


def add_new_training_in_database(data: dict | list[dict]) -> None:
    print(Training.insert_many(data).on_conflict_ignore().execute())

