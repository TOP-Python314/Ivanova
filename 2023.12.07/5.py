scores_letters = {
    'А': 1, 'В': 1, 'Е': 1, 'Ё': 1, 'И': 1, 'Н': 1, 'О': 1,
    'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2,
    'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ь': 3, 'Я': 3, 'Й': 4,
    'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ф': 8,
    'Ш': 8, 'Э': 8, 'Ю': 8, 'Щ': 10, 'Ъ': 15
}

word = input('Ввод: ')
scor = 0

for i in word:
    scor += scores_letters[i.upper()]
print(scor)

# Ввод: синхрофазатрон
# 29
