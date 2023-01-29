#                2.   Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#     (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

x, y, z = map(int, input('Введите три числа через пробел: ').split())

first_statement = not(x or y or z)
second_statements = not x and not y and not z
statement = first_statement == second_statements
print(statement)
