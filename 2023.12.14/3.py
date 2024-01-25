numbers = [1, 2, 3, 4, 5]

def numbers_strip(numbs: list[float], n: int = 1, copy: bool = False) -> list:

    if copy:
        numbs_copy = numbs[::1]
        if n > 0 and len(numbs_copy) >= n*2:
            for i in range(n):
                numbs_copy.remove(max(numbs_copy))
                numbs_copy.remove(min(numbs_copy))
            return(numbs_copy)
        else:
            return False
    else:
        if n > 0 and len(numbs) >= n*2:
            for i in range(n):
                numbs.remove(max(numbs))
                numbs.remove(min(numbs))
            return(numbs)
        else:
            return False

# > numbers
# [1, 2, 3, 4, 5]
# > test = numbers_strip(numbers
# )> test
# [2, 3, 4]
# > numbers is test
# True

# > numbers
# [1, 2, 3, 4, 5]
# > test = numbers_strip(numbers, n=2, copy=True)
# > test
# [3]
# > test in numbers
# False
# > numbers
# [1, 2, 3, 4, 5]