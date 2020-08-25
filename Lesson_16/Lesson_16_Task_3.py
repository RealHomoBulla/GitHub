'''Task 3
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.'''

class Counter:

    def __init__(self, *args):
        self.current = args[0]
        self.low = args[0]
        self.high = args[1]
        self._range = range(*args)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        result = self._range.__getitem__(index)
        if isinstance(index, slice):
            return list(result)
        else:
            return result

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

c = Counter(1, 10)

for i in c[1:10:2]:
    print(i)
