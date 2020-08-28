'''Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
of Boss class to workers list directly via access to attribute, use getters and setters instead!'''


def full_name(first, last):
    return f'{first.title()} {last.title()}'

def square_nums(lst):
    res = []
    for i in lst:
        res.append(i ** 2)
    return res



class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def __str__(self):
        return self.name

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.__workers.append(worker)

    def display_workers(self):
        if self.__workers:
            print(f'{self.name} has following workers:')
            for worker in self.__workers:
                print(worker.name)
        else:
            return None

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss
        self.__boss.add_worker(self)

    def __str__(self):
        return f'This is a worker {self.name} and his boss is {self.boss}.'

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.__boss = new_boss
            print(f'{self.name} has a new boss {self.boss}')
            new_boss.add_worker(self)
        else:
            print('Object should be a "Boss" type.')


if __name__ == '__main__':

    steve = Boss(1, 'Steve', 'Apple')
    tim = Boss(2, 'Tim', 'Apple')
    johny = Worker(3, 'Johny', 'Apple', steve)

    print(johny)
    print(johny.boss)
    johny.boss = tim
    tim.display_workers()

