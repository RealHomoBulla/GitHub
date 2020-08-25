'''Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
of Boss class to workers list directly via access to attribute, use getters and setters instead!'''

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
        print(f'{self.name} has following workers:')
        for worker in self.__workers:
            print(worker.name)

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss

    def __str__(self):
        return f'This is a worker {self.name} and his boss is {self.boss}.'

    @property
    def boss(self):
        return self.__boss.name

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.__boss = new_boss
            print(f'{self.name} has a new boss {self.boss}')
            new_boss.add_worker(self)
        else:
            print('Object should be a "Boss" type.')

steve = Boss(1, 'Steve', 'Apple')
tim = Boss(2, 'Tim', 'Apple')
johny = Worker(3, 'Johny', 'Apple', steve)

print(johny)
print(johny.boss)
johny.boss = tim
tim.display_workers()