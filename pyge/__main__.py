import argparse
import inspect
import knnge
import os
import random

from .citydb import load_cities
from .persondb import load_people

def main(args=None):
    arg_parser = argparse.ArgumentParser(description='Generate a list of people pairs.')
    arg_parser.add_argument('file', help='path to the input csv')
    args = arg_parser.parse_args()

    module_path = os.path.dirname(inspect.getfile(knnge))
    load_cities(os.path.join(module_path, 'uscities.csv'))

    people = load_people(args.file)

    while len(people) > 0:
        current_person = random.choice(people)

        people.remove(current_person)

        weights = [(p, current_person.euclidean_distance(p), current_person.coefficient(p)) for p in people]
        weighted_list = []

        for w in weights:
            weighted_list.extend([w[0]] * int(w[1] * w[2]))

        neighbor = random.choice(weighted_list)

        people.remove(neighbor)

        print(f"{current_person.name}, {neighbor.name}")


if __name__ == '__main__':
    main()
