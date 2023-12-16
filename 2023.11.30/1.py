numbers = []
while True:
    number = int(input('Введите число: '))
    if number % 7 == 0:
        numbers.append(number)
    else:
        print(' '.join(map(str, reversed(numbers))))
        break

# Введите число: 7
# Введите число: 14
# Введите число: 21
# Введите число: 28
# Введите число: 32

# 28 21 14 7
