'''
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.
'''

class Reversed_Sequence:
    def __init__(self):
        print('You can enter many strings, and they all will be added into our sequence, but in reversed way.')
        print('Enter "quit" to break a loop and see your reversed sequence: ')
        self.items = []
        self.u_input()

    def u_input(self):
        self.user_input = ''
        while True:
            self.user_input = input()
            if self.user_input == 'quit':
                break
            self.push(self.user_input)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])



sequence = Reversed_Sequence()

while not sequence.is_empty():
    print(sequence.pop())