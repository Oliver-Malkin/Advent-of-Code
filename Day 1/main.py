with open("Day 1/foods.txt", "r") as file:
    foods_raw = file.read().split('\n\n')

foods_cooked = []
for i in range(len(foods_raw)):
    temp = ' '.join(foods_raw[i].split()).split()
    total = 0
    for x in range(len(temp)):
        total += int(temp[x])
    foods_cooked.append(total)

total = 0
for i in range(0, 3):
    total += max(foods_cooked)
    foods_cooked.remove(max(foods_cooked))

print(total)