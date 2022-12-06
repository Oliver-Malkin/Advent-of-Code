with open("Day 4/input.txt", "r") as file:
    pairs = file.read().split('\n')

pairs = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split('\n')

overlapping = 0

for i in range(len(pairs)):
    pair = pairs[i].split(',') # current pair
    for j in range(0,2):
        pair[j] = pair[j].split('-')
    print(pair)

    if (int(pair[0][0]) >= int(pair[1][0]) or int(pair[0][0]) <= int(pair[1][0])):
        overlapping += 1

print(overlapping)