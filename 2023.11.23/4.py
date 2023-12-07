Chess_color1 = input("Введите координаты первой клетки: ")
Chess_color2 = input("Введите координаты второй клетки: ")
if (((((ord(Chess_color1[0]) + int(Chess_color1[1])) % 2 == 0) and ((ord(Chess_color2[0]) + int(Chess_color2[1])) % 2 == 0)) or (((ord(Chess_color1[0]) + int(Chess_color1[1])) % 2 != 0) and ((ord(Chess_color2[0]) + int(Chess_color2[1])) % 2 != 0))) and (((ord(Chess_color1[0])) <= 104 and (ord(Chess_color2[0]) <= 104)))):
      print("да")
else:
      print("нет")

 # Введите координаты первой клетки a1
 # Введите координаты второй клетки a3
 # да
 
 # Введите координаты первой клетки b1
 # Введите координаты второй клетки a3
 # нет
