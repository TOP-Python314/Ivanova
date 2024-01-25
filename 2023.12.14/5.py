@@ -0,0 +1,31 @@
def central_tendency(first : float, second : float, *numbers : float):

    numbers = [numb for numb in numbers]
    numbers += [first]
    numbers += [second]
    quantity = int(len(numbers))
    dict1 = {}
    median = sum(numbers) / quantity
    arithmetic = sum(numbers) / quantity
    geometr = 1
    harmon = 0

    for numb in numbers:
        geometr *= numb
        harmon += (1 / numb)

    geometric = geometr**(1 / quantity)
    harmonic = quantity / harmon

    dict1['median'] = median
    dict1['arithmetic'] = arithmetic
    dict1['geometric'] = geometric
    dict1['harmonic'] = harmonic

    return dict1

# > central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}

# > central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
