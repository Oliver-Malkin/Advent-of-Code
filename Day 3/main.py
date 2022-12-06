with open("Day 3/input.txt", "r") as file:
    items = file.read().split('\n')

"""
items = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']
"""

upper = ord('A')-27
lower = ord('a')-1

for i in range(len(items)):
    first = list(items[i][:int((len(items[i]))/2)])
    second = list(items[i][int((len(items[i]))/2):])
    items[i] = (first, second)

total = 0
for i in range(len(items)):
    for j in range(len(items[i][0])):
        if items[i][0][j] in items[i][1]:
            if items[i][0][j].isupper():
                total += ord(items[i][0][j]) - upper
            else:
                total += ord(items[i][0][j]) - lower
            break

print(total)