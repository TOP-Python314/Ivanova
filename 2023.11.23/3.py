input_year = int(input("Введите год: "))

if input_year % 4 == 0 and input_year % 100 != 0 and input_year % 400 != 0:
      print("Да")
else:
      print("Нет")

# Введите год: 2012
# Да

# Введите год: 2023
# Нет
