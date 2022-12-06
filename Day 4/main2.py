with open("Day 4/input.txt", "r") as file:
    pairs = file.read().split('\n')

overlapping = 0

for i in range(len(pairs)):
    pair = pairs[i].split(',') # current pair
    for j in range(0,2):
        pair[j] = pair[j].split('-')
    print(pair)

    if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]) or int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
        overlapping += 1
    elif int(pair[0][1]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1]) or int(pair[0][0]) <= int(pair[1][1]) and int(pair[1][0]) <= int(pair[0][1]):
        overlapping += 1

print(overlapping)