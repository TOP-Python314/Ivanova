King_position = input("Введите координаты фигуры: ")
King_move = input("Введите координаты хода: ")

if -1 <= (ord(King_position[0]) - ord(King_move[0])) <= 1 and -1 <= (int(King_position[1]) - int(King_move[1])) <= 1:
      print("да")
else:
      print("нет")

# Введите координаты фигуры: a1
# Введите координаты хода: b2
# да

# Введите координаты фигуры: с3
# Введите координаты хода: с5
# нет
