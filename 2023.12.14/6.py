def orth_triangle(*, hypotenuse: float = 0, cathetus1: float = 0, cathetus2: float = 0):

    if hypotenuse != 0 and cathetus1 != 0 and cathetus2 != 0:
        return None

    if hypotenuse == 0:
        result = round((cathetus1**2 + cathetus2**2)**0.5, 2)
        return result

    cathet_sum = cathetus1 + cathetus2

    if hypotenuse > cathet_sum:
        result = round((hypotenuse**2 - cathet_sum**2)**0.5, 2)
    elif hypotenuse <= cathet_sum:
        result = None
    return result

# > orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# > orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# > print(orth_triangle(cathetus2=9, hypotenuse=3))
# None