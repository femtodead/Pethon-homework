# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
#  один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

length_chocolates = int(input("Введите длинну шоколадки: "))
chocolate_bar_width = int(input("Введите ширину шоколадки: "))
number_slices = int(input("Количество долик которое планирует отломить: "))
if number_slices%length_chocolates == 0 or number_slices%chocolate_bar_width == 0:
    print(f'{length_chocolates} {chocolate_bar_width} {number_slices} -> yes')
else:
    print(f'{length_chocolates} {chocolate_bar_width} {number_slices} -> no')