#                   3.  Напишите программу, которая принимает на вход координаты точки (X и Y), 
#     причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x, y = map(int, input('Введите точки координат X и Y через пробел: ').split())

if x > 0 and y > 0: print('Первая Четверть')
elif x < 0 and y > 0: print('Вторая Четверть')
elif x < 0 and y < 0: print('Третья Четверть')
elif x > 0 and y < 0: print('Четвертая четверть')
else: print('Не вводите координаты равные 0!')
