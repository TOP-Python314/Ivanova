list1 = []
list2 = []
x = 0

num1 = input('Введите список для колонки 1: ')
num2 = input('Введите список для колонки 2: ')

list1.append(num1)
list2.append(num2)

for i in enumerate(num2):
    if i in enumerate(num1):
        x += 1

if x == len(num2):
    print('Да')
else:
    print('Нет')

# Введите список для колонки 1: 1 2 3 4
# Введите список для колонки 2: 1 2
# да

# > 1 2 3 4
# > 2 4
# нет