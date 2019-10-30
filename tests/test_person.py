from .context import knnge

import datetime
import unittest

class PersonTests(unittest.TestCase):
    def setUp(self):
        knnge.citydb.load_db('knnge/uscities.csv')

    def test_init(self):
        person = knnge.person.Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL', [])

        self.assertEqual(person.name, 'Miles Davis')
        self.assertEqual(person.dob, datetime.datetime(1926, 5, 26))
        self.assertEqual(person.gender, 'M')
        self.assertEqual(person.lat_lng, [0.216129444, -0.500846111])

        self.assertEqual(f'{person}', 'Miles Davis: 4224271779')
        self.assertEqual(hash(person), 4224271779)
        self.assertEqual(person, person)

    def test_vector(self):
        person = knnge.person.Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL', [])

        self.assertEqual(person.vector(), (0.7785535021674652, 0.0, 0.216129444, -0.500846111))

    def test_euclidean_distance(self):
        person_x = knnge.person.Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL', [])
        person_y = knnge.person.Person('Charlie Parker', '08/29/1920', 'M', 'Kansas City, KS', [])

        ed = person_x.euclidean_distance(person_y)

        self.assertEqual(ed, 0.054214132529032844)

    def test_l1_distance(self):
        person_x = knnge.person.Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL', [])
        person_y = knnge.person.Person('Charlie Parker', '08/29/1920', 'M', 'Kansas City, KS', [])

        ld = person_x.l1_distance(person_y)

        self.assertEqual(ld, 0.07455501608190737)
