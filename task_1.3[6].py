# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

number_ticket = int(input("Введите номер билета: "))
one_side_amount = number_ticket//1000
one_partys_amount = number_ticket%1000
if one_partys_amount//100+one_partys_amount%10+one_partys_amount//10%10 == one_side_amount//100+one_side_amount%10+one_side_amount//10%10:
    print(f"{number_ticket} >>> yes")
else:
    print(f"{number_ticket} >>> no")