import json
from datetime import datetime


class Config:
    start_time = 10  # 10:00
    end_time = 22  # 22:00
    min_notify_value = 0.5  # when this value is reached, notify user
    daily_target = 2.5  # Litres to drink every day


class HydratData:

    def __init__(self, ideal_hydration, current=0, daily_target=Config.daily_target):
        self.date_time = datetime.now()
        self.current = current
        self.ideal = ideal_hydration
        self.daily_target = daily_target

    def __str__(self):
        return self.to_json(as_list=False, omit_fields=[])

    def set_current_date_time(self):
        self.date_time = datetime.now()

    @staticmethod
    def from_ideal(ideal_hydration):
        return HydratData(ideal_hydration, 0)

    def with_current(self, current):
        self.current = current
        return self

    def to_json(self, as_list=False, omit_fields=None):
        if omit_fields is None:
            omit_fields = ['ideal']
        self.set_current_date_time()
        if as_list:
            return json.dumps([round(value, 3) if type(value) is float else value for key, value in self.__dict__.items() if key not in omit_fields],
                              cls=HydratEncoder)
        else:
            return json.dumps(
                {key: round(value, 3) if type(value) is float else value for key, value in self.__dict__.items() if
                 key not in omit_fields}, cls=HydratEncoder)


class HydratEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')  # Customize the date format here
        if isinstance(obj, float):
            return round(obj, 3)
        return super().default(obj)
