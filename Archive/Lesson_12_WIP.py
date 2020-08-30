# class  A:
#     def  __init__(self):
#         print('1Constructor A')
#         super().__init__()
#         print('2Constructor A')
#
# class B:
#     def __init__(self):
#         print('1Constructor B')
#         super().__init__()
#         print('2Constructor B')
#
# class C(B, A):
#     def __init__(self):
#         print('1Constructor C')
#         super().__init__()
#         print('2Constructor C')
#
#
# cc = C()


# class  A():
#     def  __init__(self):
#         self.__secret = 'password'
#
# a =  A()
# a.__dict__
#
# a._A__secret = ''
# from random import choice
#
# def privet():
#     '''
# I print Hi
#     '''
#     print('Hi')
#
# def priv():
#     print('Yo how r u?')
#
# def wazzup():
#     print('Wazzuuupp!')
#
# # print(privet.__doc__)
#
# my_hello_funcs = []
# my_hello_funcs.append(privet )
# my_hello_funcs.append(priv )
# my_hello_funcs.append(wazzup )
#
# rand_func =  choice(my_hello_funcs)
# rand_func()
#
#
# # p = privet
# # p()

