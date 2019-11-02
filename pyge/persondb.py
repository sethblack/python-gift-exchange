from .person import Person

import collections
import csv
import os
import struct
import sys


def load_people(path):
    people = []

    history = load_history(path)

    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)

        for row in reader:
            if len(row) != 4:
                print(f"{row} has incorrect format: expecting name, dob, gender, birthplace.", file=sys.stderr)
                continue

            name, dob, gender, birthplace = row
            person = Person(name, dob, gender, birthplace)
            person.exchange_history = history[hash(person)]

            people.append(person)

    return people


def load_history(path):
    history = collections.defaultdict(list)

    file_name, file_extension = os.path.splitext(path)

    history_file = f'{file_name}-history.bin'

    try:
        with open(history_file, 'rb') as f:
            p = f.read(16)

            while p:
                p_hashes = struct.unpack('QQ', p)
                history[p_hashes[0]].append(p_hashes[1])
                p = f.read(16)
    except FileNotFoundError:
        pass

    return history


def save_history(path, pairings):
    file_name, file_extension = os.path.splitext(path)

    history_file = f'{file_name}-history.bin'

    with open(history_file, 'a+b') as f:
        for (a, b) in pairings:
            f.write(struct.pack('Q', hash(a)))
            f.write(struct.pack('Q', hash(b)))
