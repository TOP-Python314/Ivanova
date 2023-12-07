First_number = int(input("Введите первое число: "))
Second_number = int(input("Введите второе число: "))

if  Second_number != 0: # Чтобы не было ситуации деления на ноль 
      if First_number % Second_number == 0:
            print(First_number, "делится на", Second_number, "нацело", """
Частное:""", (int(First_number / Second_number)))
      else:
            print(First_number, "не делится на", Second_number, "нацело", """
неполное частное:""", (int(First_number // Second_number)), """
остаток:""", (int(First_number % Second_number)))
else:
      print ("Некорректный ввод")

# Введите первое число: 8
# Введите второе число: 2
# 8 делится на 2 нацело
# Частное: 4

# Введите первое число: 1
# Введите второе число: 0
# Некорректный ввод
