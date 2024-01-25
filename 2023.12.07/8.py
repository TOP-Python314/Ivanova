names = input('Ввод: ').split('; ')
names_dict = {}
names_list = []
for i in names:
    if i in names_dict:
        hof = names_dict[i] + 1
        num = i.find('.')
        test = i[0:num] + '_' + str(hof )+ i[num:]
        names_list.append(test)
    else:
        names_list.append(i)
    names_dict[i] = names_dict.get(i, 0) + 1
    names_list.sort()
for j in names_list:
    print(j)


# Ввод: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main.py
# src.tar.gz
# src_2.tar.gz