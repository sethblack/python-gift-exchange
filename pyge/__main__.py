import argparse
import inspect
import pyge
import os
import random

from .citydb import load_cities
from .persondb import load_people
from .persondb import save_history, load_history

def main():
    arg_parser = argparse.ArgumentParser(description='Generates a list of people pairings for a holiday gift exchange.')

    arg_parser.add_argument('file', help='path to the csv containing a list of people who want to be part of the celebration')
    arg_parser.add_argument(
        '-s', '--save-history',
        help='save a history file of matches',
        dest='save_history',
        action='store_true'
    )
    arg_parser.add_argument(
        '-n', '--no-history',
        help='do not save a history file of matches',
        dest='save_history',
        action='store_false'
    )
    arg_parser.add_argument(
        '-c', '--citydb',
        help='path to city csv for distance calculations',
        default=None,
        metavar='citydb',
        dest='citydb'
    )
    arg_parser.add_argument(
        '-l', '--history-length',
        help='number of cycles before people can be paired again',
        default=3,
        type=int,
        metavar='historylength',
        dest='history_length'
    )

    arg_parser.set_defaults(save_history=True)

    args = arg_parser.parse_args()

    if args.citydb:
        load_cities(args.citydb)
    else:
        module_path = os.path.dirname(inspect.getfile(pyge))
        load_cities(os.path.join(module_path, 'uscities.csv'))

    people_static = load_people(args.file, args.history_length)
    people_a = list(people_static)
    people_b = list(people_static)

    pairs = []

    while len(people_a) > 0:
        gifter = random.choice(people_a)

        weights = [(p, gifter.euclidean_distance(p), gifter.coefficient(p)) for p in people_b]
        weighted_list = []

        for w in weights:
            weighted_list.extend([w[0]] * int(w[1] * w[2]))

        if len(weighted_list) == 0:
            if len(pairs) == 0:
                raise Exception('Could not match set.')

            (prev_a, prev_b) = pairs.pop()

            people_a.append(prev_a)
            people_b.append(prev_b)

            continue

        giftee = random.choice(weighted_list)

        people_a.remove(gifter)
        people_b.remove(giftee)

        pairs.append((gifter, giftee))

    for (gifter, giftee) in pairs:
        print(f"{gifter.name}, {giftee.name}")

    if args.save_history:
        save_history(args.file, pairs)


if __name__ == '__main__':
    main()
