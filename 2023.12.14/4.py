def countable_nouns(number: int, words: tuple[str, str, str]) -> str:
    number_str = str(number)
    if number != 11 and number_str.endswith('1'):
        return words[0]
    elif number_str.endswith('2') and number != 12 or number_str.endswith('3') and number != 13 or number_str.endswith('4') and number != 14:
        return words[1]
    else:
        return words[2]

# > countable_nouns(1, ("год", "года", "лет"))
# 'год'
# > countable_nouns(2, ("год", "года", "лет"))
# 'года'
# > countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# > countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# > countable_nouns(22, ("год", "года", "лет"))
# 'года'