class SerialNumbers:
    def __init__(self, prefix='COMP', len=10):
        self.__prefix = prefix
        self.__len = len
        self.__CODE = ['AW', 'FY', 'RE']
        self.__code_pos = 0
        self.__current_num =  0

    def __iter__(self):
        return self

    def __next__(self):
        ret_str = self.__prefix + self.__CODE[self.__code_pos] +  str(self.__current_num)

        if self.__current_num < self.__len:
            self.__current_num += 1
        else:
            self.__current_num = 0
            self.__code_pos += 1

        if self.__code_pos >= len(self.__CODE):
            raise StopIteration

        return ret_str


for num in SerialNumbers():
    print(num)