digit_list = list(range(0, 101))
result_list = []
i = 0
print(digit_list)
while i < len(digit_list):
    while digit_list[i] % 7 == 0 and digit_list[i] % 5 != 0:
        result_list.append([i])
        break
    i += 1
print(result_list)

# list_1_to_100 = list(range(0, 100))
# list_special_numbers = []
# i = 0
#
# while i < len(list_1_to_100):
#     while list_1_to_100[i] % 7 == 0 and list_1_to_100[i] % 5 != 0:
#         list_special_numbers.append([i])
#         break
#     i += 1
#print(list_special_numbers)