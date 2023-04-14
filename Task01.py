# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

coin = int(input("Enter quantity: "))
for el in range(1, coin + 1):
    count = 0
    count2 = 0
    i = 0
    n = int(input())

while (n == 0):
    count = count + 1
    i = i + 1

    while (n == 1):
        count2 = count2 + 1

    if count < count2:
        print(count)
        elif count2 < count:
        print(count2)
