userinsert_1 = int(input("Введите мили: "))
userinsert_2 = int(input("Введите доли: "))
calculation_process = userinsert_1 + (userinsert_2 / 10)

print(calculation_process, "миль =",  round(calculation_process * 1.61, 1), "км")

# Введите мили: 18
# Введите доли: 9

# 18.9 миль = 30.4 км
