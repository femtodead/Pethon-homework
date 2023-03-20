# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

number_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
number = int(input("Введите число: "))
number_difference = number_list[0]-number
count_number = 0
for elements in number_list:
    if abs(number_difference) >= abs(elements-number):
        number_difference = elements-number
        count_number = elements
print(count_number)
# не понятно почему во втором варианте должно выдавать 10, хотя 8 тоже подходит - ниже приведен вариант где будет выводить 10
# number_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# number = int(input("Введите число: "))
# number_difference = number_list[0]-number
# count_number = number_list[0]
# for index in range(1,len(number_list)):
#     print(F"первая разница{abs(number_difference)} вторая {abs(number_list[index]-number)}")
#     if abs(number_difference) >= abs(number_list[index]-number):
#         if abs(number_difference) != abs(number_list[index]-number):
#             number_difference = number_list[index]-number
#             count_number = number_list[index]
# print(count_number)
