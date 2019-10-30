import inspect
import knnge
import os
import random

from .citydb import load_db
from .person import Person

def main(args=None):
    module_path = os.path.dirname(inspect.getfile(knnge))
    load_db(os.path.join(module_path, 'uscities.csv'))

    people = [
        Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL', []),
        Person('Charlie Parker', '08/29/1920', 'M', 'Kansas City, KS', []),
        Person('John Coltrane', '09/23/1926', 'M', 'Hamlet, NC', []),
        Person('Herbie Hancock', '04/12/1940', 'M', 'Chicago, IL', []),
        Person('Louis Armstrong', '08/04/1901', 'M', 'New Orleans, LA', []),
        Person('Dizzy Gillespie', '10/21/1917', 'M', 'Cheraw, SC', []),
        Person('Duke Ellington', '04/29/1899', 'M', 'Washington, DC', []),
        Person('Bill Evans', '08/16/1929', 'M', 'Plainfield, NJ', []),
        Person('Billie Holiday', '04/07/1915', 'F', 'Philadelphia, PA', []),
        Person('Ella Fitzgerald', '04/25/1917', 'F', 'Newport News, VA', []),
        Person('Sarah Vaughan', '03/27/1924', 'F', 'Newark, NJ', []),
        Person('Nina Simone', '02/21/1933', 'F', 'Tryon, NC', []),
    ]

    while len(people) > 0:
        current_person = random.choice(people)

        people.remove(current_person)

        print(current_person)

        neighbor = random.choice(sorted(
            [(p, current_person.euclidean_distance(p)) for p in people],
            key=lambda f: f[1],
            reverse=True
        )[:3])

        people.remove(neighbor[0])

        print('\t', neighbor[0])


if __name__ == '__main__':
    main()
