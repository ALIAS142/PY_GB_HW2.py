# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Enter number: "))
# for i in range(1, N + 1):
k = 0
a = 2 ** k
while a < N:
    print(a)
k = k + 1

