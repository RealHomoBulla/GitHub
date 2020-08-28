import unittest
import workers

# I wanted to test some random function to see that functions tests also work well.
class SquaresTestCase(unittest.TestCase):
    def test_squares(self):
        lst_to_test = [1, 2, 3, 4]
        lst_tested = workers.square_nums(lst_to_test)
        self.assertEqual(lst_tested, [1, 4, 9, 16], 'Squared List is not same as expected')

# Now I test classes from my program.
class BossTestCase(unittest.TestCase):
    def setUp(self):
        # Creating class instance.
        self.bill = workers.Boss(5, 'Bill', 'Microsoft')

        # Creating instance of class with wrong types of data (string as ID, numbers as Name and Company.
        # self.carl = workers.Boss('Fake ID', 123, 'Microsoft')

    def test_type(self):
        self.assertIsInstance(self.bill, workers.Boss, 'Not an instance of Boss class.')

    def test_attributes(self):
        # Testing if name was recorded the right way.
        self.assertEqual(self.bill.name, 'Bill')
        # Testing if wrong ID type will throw an error.
        self.assertIsInstance(self.bill.id, int, 'ID is not a number. There must be a mistake.')
        # Testing if wrong Name type will throw an error.
        self.assertIsInstance(self.bill.name, str, 'Name is not a string. There must be a mistake.')
        # Testing if wrong Company type will throw an error.
        self.assertIsInstance(self.bill.company, str, 'Company is not a string. There must be a mistake.')
        # Testing if initially the workers list is empty.
        self.assertIsNone(self.bill.display_workers, 'There are some workers in the list on creation. It should be empty.')

        # Create a worker for him to test some methods.
        self.johny = workers.Worker(3, 'Johny', 'Microsoft', self.bill)
        # And we check if worker was added to Boss Bill workers list.
        self.assertIsNotNone(self.bill.display_workers, 'There are still no workers in the list after adding.')

        # We add another company to test what happens if worker change the job.
        self.steve = workers.Boss(7, 'Steve', 'Apple')
        # add another worker to Microsoft to  check what  happens  if he changes the job.
        self.mike = workers.Worker(8, 'Mike', 'Microsoft', self.bill)
        # Trying to test the method.
        self.steve.add_worker(self, self.mike)
        self.assertIsNotNone(self.steeve.workers, 'Worker was not added.')


class WorkerTestCase(unittest.TestCase):
    def setUp(self):
        self.bill = workers.Boss(5, 'Bill', 'Microsoft')
        # Creating an instance of Worker class.
        self.johny = workers.Worker(3, 'Johny', 'Microsoft', self.bill)

    def test_type(self):
        self.assertIsInstance(self.johny, workers.Worker, 'Not an instance of Worker class.')

    def test_attributes(self):
        # Testing if some attribute (ID) was recorded the right way.
        self.assertEqual(self.johny.id, 3)
        # Testing if wrong ID type will throw an error.
        self.assertIsInstance(self.johny.id, int, 'ID is not a number. There must be a mistake.')
        # Testing if wrong Name type will throw an error.
        self.assertIsInstance(self.johny.name, str, 'Name is not a string. There must be a mistake.')
        # Testing if wrong Company type will throw an error.
        self.assertIsInstance(self.johny.company, str, 'Company is not a string. There must be a mistake.')
        # Check if his boss is of class Boss
        self.assertEqual(self.johny.boss.name, 'Bill', 'Boss was added in wrong way.')
        # Boss and the worker should work for the same company.
        self.assertEqual(self.johny.boss.company, self.johny.company, 'They work in different company')



if __name__ == "__main__":
    unittest.main()
