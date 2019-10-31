from .person import Person

import csv
import sys


def load_people(path):
    people = []

    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)

        for row in reader:
            if len(row) != 4:
                print(f"{row} has incorrect format: expecting name, dob, gender, birthplace.", file=sys.stderr)
                continue

            name, dob, gender, birthplace = row
            people.append(Person(name, dob, gender, birthplace))

    return people
