First_number =  int(input("Введите первое число: "))
Second_number = int(input("Введите второе число: "))
Fird_number =   int(input("Введите третье число: "))

if    First_number < 0 and Second_number > 0 and Fird_number > 0:
      print("Сумма положительных:", Second_number + Fird_number)
elif Second_number < 0 and First_number > 0 and Fird_number > 0:
      print("Сумма положительных:", First_number + Fird_number)
elif Fird_number < 0 and First_number > 0 and Second_number > 0:
      print("Сумма положительных:", Second_number + First_number)
elif First_number < 0 and Second_number < 0 and Fird_number > 0:
      print("Единственное положительное:", Fird_number)
elif First_number > 0 and Second_number < 0 and Fird_number < 0:
      print("Единственное положительное:", First_number)
elif First_number < 0 and Second_number > 0 and Fird_number < 0:
      print("Единственное положительное:", Second_number)
elif First_number > 0 and Second_number > 0 and Fird_number > 0:
      print ("Сумма положительных:", Fird_number + Second_number + Fird_number)
else:
      print("Все числа ввода отрицательные")

# Введите первое число: 2
# Введите второе число: -1
# Введите третье число: -3
# Единственное положительное: 2

# Введите первое число: -2
# Введите второе число: 1
# Введите третье число: 3
# Сумма положительных: 4

# Введите первое число: 2
# Введите второе число: 1
# Введите третье число: 3
# Сумма положительных: 6

# Введите первое число: -2
# Введите второе число: -1
# Введите третье число: -3
# Все числа отрицательные
