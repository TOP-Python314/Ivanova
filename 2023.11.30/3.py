num = int(input('Введите число: '))
summ = 0
for i in range(1, num + 1):
    if num % i == 0:
        summ += i
print(summ)

# Введите число: 8
# 15
