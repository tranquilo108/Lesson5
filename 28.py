# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Input: 2 2
# Output: 4

# def sum_of(x, y):
#     if y == 0:
#         return x
#     return sum_of(x + 1, y - 1)
# print(sum_of(21,22))

print((sum_of := lambda x, y: x if y == 0 else sum_of(x + 1, y - 1))(int(input('x = ')), int(input('y = '))))