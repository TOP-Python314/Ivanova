def strong_password(password) -> bool:
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numb = 0 
    symb = False

    for i in password:
        for j in numbers:
            if i == j:
                numb += 1

    for char in "!@-#$' '%_&:;":
        if char in password:
            symb = True

    if len(password) <= 8:
        return False
    elif password.upper() == password:
        return False
    elif password.lower() == password:
        return False
    elif numb <= 1:
        return False
    elif symb != True:
        return False
    else:
        return True
        
        
# > strong_password('AaRythm!8')
# True
# > strong_password('password')
# False