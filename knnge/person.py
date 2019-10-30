import hashlib

from datetime import datetime
from .citydb import lookup_city


class Person():
    def __init__(self, name, dob, gender, city, exchange_history):
        self.name = name
        self.dob = datetime.strptime(dob, '%m/%d/%Y')
        self.gender = gender
        self.lat_lng = lookup_city(city)
        self.exchange_history = exchange_history

    def vector(self):
        age_point = self.age_in_days / 43830.
        gender_point = 0. if self.gender == 'M' else 1.

        return (age_point, gender_point, self.lat_lng[0], self.lat_lng[1])

    def euclidean_distance(self, other):
        x_vector = self.vector()
        y_vector = other.vector()

        return sum([(x - y) ** 2 for x, y in zip(x_vector, y_vector)]) ** .5

    def l1_distance(self, other):
        x_vector = self.vector()
        y_vector = other.vector()

        return sum([abs(x - y) for x, y in zip(x_vector, y_vector)])

    @property
    def age_in_days(self):
        return (datetime.now() - self.dob).days

    def __str__(self):
        return f'{self.name}: {self.__hash__()}'

    def __hash__(self):
        return int(hashlib.md5(
            f'{self.name}:{self.dob}:{self.gender}:{self.lat_lng}'.encode('utf-8')
        ).hexdigest()[:8], 16)

    def __eq__(self, other):
        return type(self) == type(other) and self.__hash__() == other.__hash__()
