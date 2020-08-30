from unittest import TestCase
import funcstotest

class NameTestCase(TestCase):

    def test_first_and_last_names(self):
        full1 = funcstotest.full_name('Carl', 'Johnson')
        full2 = funcstotest.full_name('cARL', 'jOHNSON')
        self.assertEqual(full1, 'Carl Johnson')
        self.assertEqual(full2, 'Carl Johnson')

class SquaresTestCase(TestCase):

    def test_squares(self):
        lst_to_test = [1, 2, 3, 4]
        lst_tested = funcstotest.square_nums(lst_to_test)
        self.assertEqual(lst_tested, [1, 4, 9, 16])

