import random
import statistics

# 1א

cities: list[str] = ['Tokyo', 'New York', 'Paris', 'London', 'Sydney', 'Dubai', 'Shanghai']

# a
print(sorted(cities, key=lambda city: len(city)))

# b
print(sorted(cities, key=lambda city: city.split()))

# c
print(sorted(cities, key=lambda city: city[-1]))

# d
print(sorted(cities, key=lambda city: city[-1], reverse=True))

# e
print(sorted(cities, key=lambda city: city.lower().count('a')))

# f

cities_dist: [str | int] = [['Tokyo', 5760, 'Asia'], ['New York', 5690, 'North America'],
                            ['Paris', 2050, 'Europe'], ['London', 2240, 'Europe'],
                            ['Sydney', 8780, 'Australia'], ['Dubai', 1300, 'Asia'],
                            ['Shanghai', 4920, 'Asia']]

# א
print(sorted(cities_dist, key=lambda c: c[1]))

# ב
print(sorted(cities_dist, key=lambda c: c[1], reverse=True))

# ג
print(sorted(cities_dist, key=lambda c: c[2]))

# ד
print(sorted(cities_dist, key=lambda c: (c[2], c[1])))



# 1ב

rand_num: list[int] = [random.randint(1, 100) for _ in range(50)]

# 1
print(sorted(rand_num, key=lambda x: x))

# 2
avg: float = statistics.mean(rand_num)
print(sorted(rand_num, key=lambda x: (x - avg)))
for num in rand_num:
    print(f'number: {num}, the distance from avg: {avg:.2f}')
