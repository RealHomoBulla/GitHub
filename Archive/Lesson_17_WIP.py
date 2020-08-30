import unittest
from homework10.phonebook import Car, Engine, EngineBenzin, EngineDiesel,


class MyTest(unittest.TestCase):
    def test_car_create_valis(self):
        eng = EngineBenzin(40)
        car  = Car('Name', eng)
        self.assertEqual(car.name, 'Name', 'Name is wrong!')
        self.assertFalse(car.stops, 'Why stops are on?')

unittest.main()
