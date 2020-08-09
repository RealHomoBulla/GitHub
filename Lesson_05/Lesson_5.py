full_name = 'Shargorodksyi Andrii Igorovych'
last_name, first_name, father_name = full_name.split(' ')
print(last_name)
print(first_name)
print(father_name)

test = ['Ivan', 'Petro', 'Bohdan']
test.append('Drus')
print(test)

new_users = ['Nastya', 'Olya', 'Katya']
# Append is not suitable to add like this, because it will put
# all objects and one list item


arr = [1, 2, 3, 4, 5]
print(arr)
arr.append(12)
print(arr)
arr_1 = ['33', '14', '88']
print(arr_1)
arr.insert(0, arr_1)
print(arr)
arr_1.append(7)
print(arr_1)
print(arr)
