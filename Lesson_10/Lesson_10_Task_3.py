'''
Task 3
TV controller

Create a simple prototype of a TV controller in Python.'''

class TV_Controller:

    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.chosen_channel = 0

    def first_channel(self):
        self.chosen_channel = 0
        print(self.channel_list[0])

    def last_channel(self):
        self.chosen_channel = len(self.channel_list) - 1
        print(self.channel_list[-1])

    def turn_channel(self, number):
        if len(self.channel_list) > number > 1:
            self.chosen_channel = number - 1
            print(self.channel_list[self.chosen_channel])
        else:
            print('Number is out of range.')

    def next_channel(self):
        self.chosen_channel += 1
        if self.chosen_channel >= len(self.channel_list):
            self.chosen_channel = 0
            print(self.channel_list[self.chosen_channel])
        else:
            print(self.channel_list[self.chosen_channel])

    def prev_channel(self):
        self.chosen_channel -= 1
        if self.chosen_channel < 0:
            self.chosen_channel = len(self.channel_list) - 1
            print(self.channel_list[self.chosen_channel])
        else:
            print(self.channel_list[self.chosen_channel])

    def current_channel(self):
        print(f'You are currently watching channel "{self.channel_list[self.chosen_channel]}".')

    def is_exist(self, check):
        self.check = str(check)
        if self.check.isdigit():
            if len(self.channel_list) > int(self.check) - 1 > 1:
                print(f'The channel "{int(self.check)}" is present in the list of channels.')
                print(f'It is "{channel_list[int(self.check)-1]}" channel.')
            else:
                print(f'You don\'t have channel "{self.check}".')
        elif self.check.lower() in [c.lower() for c in self.channel_list]:
            i = 1
            for c in self.channel_list:
                if c.lower() == self.check.lower():
                    print(f'The channel "{self.check}" is present in the list of channels.')
                    print(f'It is number {i}.')
                else:
                    i += 1
        else:
            print(f'You don\'t have channel "{self.check}".')


channel_list = ['BBC', 'Discovery', 'TV-1000', 'MTV', 'MKBHD', 'Jackie Chan']
tv_controller = TV_Controller(channel_list)


tv_controller.first_channel()
tv_controller.next_channel()
tv_controller.last_channel()
# It will go from last_channel to first_channel
tv_controller.next_channel()
# And can go back from first_channel to last_channel
tv_controller.prev_channel()
tv_controller.first_channel()
tv_controller.turn_channel(2)
# Also it prints if the channel is out of range.
tv_controller.turn_channel(8)
tv_controller.current_channel()
# I made this function case-insensitive. Also, it prints what is the number of the channel found by name.
tv_controller.is_exist('bbc')
# And this function prints the name of the channel found by number.
tv_controller.is_exist(6)
tv_controller.is_exist('MTV')
# Prints that you don't have some channels.
tv_controller.is_exist('Tarantino_TV')
tv_controller.is_exist(7)



