# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


S = int(input("Enter sum "))
M = int(input("Enter mult "))
x1 = int(1)
x2 = int(1)
y1 = int(S - x1)
y2 = int(M / x2)

S = int(x1 + y1)
M = int(x2 * y2)

while y1 != y2:
          x1 += 1
          x2 += 1
          y1 = S - x1
          y2 = M / x2
          print(x1, x2, y1, y2)


