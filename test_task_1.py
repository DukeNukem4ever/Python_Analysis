##### ЧАСТЬ 1 #####

lis = [int(i) for i in input().split(', ')]

# Задание 1

lis2 = []

for i in lis:
    if i % 2 == 0:
        lis2.append(i)
    else:
        continue

print("Четные числа: " + str(lis2))

# Задание 2

print("Максимальное число: %s" % max(lis))
print("Минимальное число: %s" % min(lis))

# Задание 3

lis_sort = []

lis2 = lis.copy()

for i in range(len(lis)):
    lis_sort.append(min(lis2))
    lis2.remove(min(lis2))

print("Отсортированный список: " + str(lis_sort))