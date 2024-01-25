def taxi_cost(distance, w_time = 0) -> int | None:
    if distance < 0:
        print(None)
    else:
        return (round(base + ((distance/150) * add) + (w_time * 3)))

base = 80
add = 6

# >>> taxi_cost(1800)
# 152
# >>> taxi_cost(0, 8)
# 104
# >>> taxi_cost(30000, 15)
# 1325
# >>> taxi_cost(-500)
# None