code = input('Ввод: ')
data = {}

while True:
    if code == '':
        print(code.upper())
        code = input('Ввод: ')
        keys = list(filter(lambda key: data[key] == code, data))
        for i in data.values():
            for j in i:
                if code in i:
                    print(*keys, sep=' ')
                else:
                    print('! value error !')
                break
            break
        break    
    elif code == ' ':
        data[code] = code[1:4]
    else:
        data[code[0:4]] = code[5:]
        code = input('Ввод: ')

# Ввод: 1022 ER_DUP_KEY
# Ввод: 1016 ER_CANT_OPEN_FILE
# Ввод: 1010 ER_DB_DROP_RMDIR
# Ввод: 1008 ER_DB_DROP_EXISTS
# Ввод:

# Ввод: ER_DUP_KEY
# 1022


# Ввод: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Ввод: 4108 ER_GIPK_COLUMN_EXISTS
# Ввод: 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# >

# Ввод: ER_CANT_OPEN_FILE
# ! value error !