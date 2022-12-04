with open("Day 3/input.txt", "r") as file:
    items = file.read().split('\n')

items = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw',]

upper = ord('A')-27
lower = ord('a')-1

for i in range(len(items)):
    first = list(items[i][:int((len(items[i]))/2)])
    second = list(items[i][int((len(items[i]))/2):])
    items[i] = (first, second)

for i in range(len(items)):
    print(items[i])
