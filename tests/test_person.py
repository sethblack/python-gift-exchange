from .context import pyge

from unittest import TestCase

import datetime

class PersonTests(TestCase):
    def setUp(self):
        pyge.citydb.load_cities('pyge/uscities.csv')

    def test_init(self):
        person = pyge.person.Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL')

        self.assertEqual(person.name, 'Miles Davis')
        self.assertEqual(person.dob, datetime.datetime(1926, 5, 26))
        self.assertEqual(person.gender, 'M')
        self.assertEqual(person.lat_lng, [0.216129444, -0.500846111])

        self.assertEqual(f'{person}', 'Miles Davis: 4224271779')
        self.assertEqual(hash(person), 4224271779)
        self.assertEqual(person, person)

    def test_vector(self):
        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=3650)

        person = pyge.person.Person(
            'Miles Davis',
            yesterday.strftime('%m/%d/%Y'),
            'M',
            'Alton, IL'
        )

        self.assertEqual(person.vector(), (0.08327629477526809, 0.0, 0.216129444, -0.500846111))

    def test_euclidean_distance(self):
        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=3650)

        person_x = pyge.person.Person('Miles Davis', yesterday.strftime('%m/%d/%Y'), 'M', 'Alton, IL')
        person_y = pyge.person.Person('Charlie Parker', yesterday.strftime('%m/%d/%Y'), 'M', 'Kansas City, KS')

        ed = person_x.euclidean_distance(person_y)

        self.assertEqual(ed, 0.025540398792728482)

    def test_l1_distance(self):
        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days=3650)

        person_x = pyge.person.Person('Miles Davis', yesterday.strftime('%m/%d/%Y'), 'M', 'Alton, IL')
        person_y = pyge.person.Person('Charlie Parker', yesterday.strftime('%m/%d/%Y'), 'M', 'Kansas City, KS')

        ld = person_x.l1_distance(person_y)

        self.assertEqual(ld, 0.02673388900000004)

    def test_coefficient(self):
        person_x = pyge.person.Person('Miles Davis', '05/26/1926', 'M', 'Alton, IL')
        person_y = pyge.person.Person('Charlie Parker', '08/29/1920', 'M', 'Kansas City, KS')
        person_z = pyge.person.Person('John Coltrane', '09/23/1926', 'M', 'Hamlet, NC')

        person_x.add_history(person_y)
        person_y.add_history(person_z)

        self.assertTrue(person_x.has_history(person_y))
        self.assertFalse(person_x.has_history(person_z))

        c1 = person_x.coefficient(person_y)
        self.assertEqual(c1, 0.)

        c2 = person_y.coefficient(person_x)
        self.assertEqual(c1, 0.)

        c3 = person_x.coefficient(person_z)
        self.assertEqual(c3, 1000.)
