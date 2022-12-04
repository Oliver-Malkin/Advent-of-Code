with open("Day 3/input.txt", "r") as file:
    items = file.read().split('\n')

'''
items = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']
'''

upper = ord('A')-27
lower = ord('a')-1

elves = []
for i in range(0, len(items), 3):
    elves.append((list(items[i]), list(items[i+1]), list(items[i+2])))

total = 0
for i in range(len(elves)):
    for j in range(len(elves[i][0])):
        if elves[i][0][j] in elves[i][1] and elves[i][0][j] in elves[i][2]:
            if elves[i][0][j].isupper():
                total += ord(elves[i][0][j]) - upper
            else:
                total += ord(elves[i][0][j]) - lower
            break

print(total)