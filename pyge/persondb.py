from .person import Person

import collections
import time
import csv
import os
import struct
import sys


def load_people(path, history_length=3):
    people = []

    history = load_history(path, history_length=3)

    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)

        for row in reader:
            if len(row) != 4:
                print(f"{row} has incorrect format: expecting name, dob, gender, birthplace.", file=sys.stderr)
                continue

            name, dob, gender, birthplace = row
            person = Person(name, dob, gender, birthplace)
            person.exchange_history = history.get(hash(person), [])

            people.append(person)

    return people


def load_history(path, history_length=3):
    file_name, file_extension = os.path.splitext(path)

    history_file = f'{file_name}-history.bin'
    history_cycles = collections.defaultdict(list)

    try:
        with open(history_file, 'rb') as f:
            p = f.read(24)

            while p:
                cycle, person_a, person_b = struct.unpack('QQQ', p)

                history_cycles[cycle].append((person_a, person_b))

                p = f.read(24)
    except FileNotFoundError:
        return {}

    history = collections.defaultdict(list)

    for cycle_no in sorted(history_cycles.keys())[(history_length * -1):]:
        for pairing in history_cycles[cycle_no]:
            history[pairing[0]].append(pairing[1])

    return dict(history)


def save_history(path, pairings):
    file_name, file_extension = os.path.splitext(path)

    history_file = f'{file_name}-history.bin'

    cycle = int(time.time())

    with open(history_file, 'a+b') as f:
        for (a, b) in pairings:
            f.write(struct.pack('QQQ', cycle, hash(a), hash(b)))
