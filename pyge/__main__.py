import argparse
import inspect
import pyge
import os
import random

from .citydb import load_cities
from .persondb import load_people
from .persondb import save_history

def main():
    arg_parser = argparse.ArgumentParser(description='Generate a list of people pairs.')
    arg_parser.add_argument('file', help='path to the input csv')
    args = arg_parser.parse_args()

    module_path = os.path.dirname(inspect.getfile(pyge))
    load_cities(os.path.join(module_path, 'uscities.csv'))

    people_a = load_people(args.file)
    people_b = list(people_a)

    pairs = []

    while len(people_a) > 0:
        gifter = random.choice(people_a)

        people_a.remove(gifter)

        weights = [(p, gifter.euclidean_distance(p), gifter.coefficient(p)) for p in people_b]
        weighted_list = []

        for w in weights:
            weighted_list.extend([w[0]] * int(w[1] * w[2]))

        giftee = random.choice(weighted_list)

        people_b.remove(giftee)

        pairs.append((gifter, giftee))

        print(f"{gifter.name}, {giftee.name}")

    save_history('history.pkl', pairs)


if __name__ == '__main__':
    main()
