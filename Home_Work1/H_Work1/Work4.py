#                         Напишите программу, которая по заданному номеру четверти, 
#                   показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти от 1 до 4: '))

if number == 1: print('Диапазон координат при: x > 0, y > 0')
elif number == 2: print('Диапазон координат при: x < 0, y > 0')
elif number == 3: print('Диапазон координат при: x < 0, y < 0')
elif number == 4: print('Диапазон координат при: x > 0, y < 0')
else: print('Ошибка диапазона чисел! Введите числа От 1 До 4')
