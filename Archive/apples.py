import unittest


class Food(object):
    def __init__(self):
        self.consumed = False

    def consume(self):
        self.consumed = True


class Fruit(Food):
    def __init__(self):
        super(Fruit, self).__init__()
        self.been_cut = False

    def cut(self):
        print("cut the fruit")
        self.been_cut = True


class Consumer(object):
    def __init__(self):
        self.apple = Fruit()
        self.banana = Fruit()

    def consume_food(self):
        food = self.pick_food()
        food.cut()
        print("consuming the food")
        food.consume()

    def pick_food(self):
        return self.apple


class TestConsumer(unittest.TestCase):

    def test_consume_food_consumes_the_apple(self):
        c = Consumer()
        c.consume_food()
        self.assertTrue(c.apple.consumed,
                        "Expected apple to be consumed")

    def test_consume_food_cuts_the_food(self):
        c = Consumer()
        c.consume_food()
        self.assertTrue(c.apple.been_cut,
                        "Expected apple to be cut")

    def test_pick_food_always_selects_the_apple(self):
        c = Consumer()
        food = c.pick_food()
        self.assertEqual(c.apple, food,
                          "Expected apple to have been picked")


if __name__ == '__main__':
    unittest.main()