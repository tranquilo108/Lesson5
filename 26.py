# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def sqrt(n,m):
#     if m == 1:
#         return n
#     return n * (sqrt(n, m - 1))


print((sqrt := lambda n, m: n if m == 1 else n * sqrt(n, m - 1))(int(input('n = ')), int(input('m = '))))