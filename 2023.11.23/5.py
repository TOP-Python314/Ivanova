Rook_position = input("Введите координаты фигуры: ")
Rook_move = input("Введите координаты хода фигуры: ")

if (((ord(Rook_position[0])) == (ord(Rook_move[0]))) or ((int(Rook_position[1])) == (int(Rook_move[1])))):
      print("да")
else:
      print("нет")
