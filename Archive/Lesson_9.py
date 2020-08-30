# import json
# with open('cj.json')  as file_object:
#     cj = json.load(file_object)
#
# for k,v in cj.items():
#     print(k, ':', v)

# import json
# cj = {}
# cj['first_name'] = 'Carl'
# cj['last_name'] = 'Jonhson'
# cj['cars'] = [{'brand': 'Chevrolet',
#             'model': '1964 Impala',
#             'color': 'black'},
#            {'brand': 'Ferrari',
#             'model': '1987 Testarossa',
#             'color': 'white'}]
# cj['has_a_dog'] = True
# cj['money_in_pockets'] = 500
#
# with open('cj.json', 'w') as file_object:
#  json.dump(cj, file_object)

# with open('user_info.txt') as file_oject:
#     username = file_oject.read()
# print('Hello, and welcome back, ' + username + '!')

# username = input('What is your name?: ')
# with open('user_info.txt', 'w') as file_oject:
#     file_oject.write(username)

# with open('weekdays.txt') as week_file:
#     weekdays  = [day.rstrip() for day in week_file.readlines()]
# print(weekdays)

# with open('weekdays.txt') as f:
#     print(f.readline())
#     print(f.readline())

# with open('weekdays.txt') as f:
#     for line in f:
#         print(line, end='')

# def get_phone_book():
#     try:
#         with open
#
#     return [
#         {'name': 'Андрей', 'phone': '0930423834'},
#         {'name': 'Андрей', 'phone': '0930423834'},
#         {name': 'Андрей', 'phone': '0930423834'}
#     ]
#
# phonebook = get_phone_book(