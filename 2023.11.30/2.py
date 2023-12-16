numbers = []
x = 0
while x < 5 :
    x += 1
    number = int(input("Введите число: "))
    if number > 0:
        numbers.append(number)
    else:
        number == 0
    if x == 5:
        print(sum(numbers))

# Введите число: 2
# Введите число: 4
# Введите число: -5
# Введите число: 11
# Введите число: -7
# 17
