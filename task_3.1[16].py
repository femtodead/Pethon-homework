# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2

# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# (*) Усложнение. При выводе результата на экран воспользуйтесь тернарным оператором.

number = int(input("Введите число: "))
my_list = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
count_number = 0
for element in my_list:
   count_number += 1 if element == number else 0
print(f"{-1 if count_number == 0 else count_number}")