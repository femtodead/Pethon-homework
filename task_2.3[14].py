# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8

number = (int(input("Введите число: ")))
number_power = 0
while True:
    if 2**number_power > number: break
    else: 
        print(2**number_power, end = " ")
        number_power += 1