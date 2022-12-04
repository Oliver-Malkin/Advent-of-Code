with open("Day 2/input.txt", "r") as file:
    moves = file.read().split('\n')

#moves = ['A Y', 'B X', 'C Z']

scores = {
    'X': 1, # Rock      lose
    'Y': 2, # Paper     draw
    'Z': 3  # Scissors  win
}

outcome = {
    'A X': 3+scores['X'],
    'A Y': 6+scores['Y'],
    'A Z': 0+scores['Z'],
    'B X': 0+scores['X'],
    'B Y': 3+scores['Y'],
    'B Z': 6+scores['Z'],
    'C X': 6+scores['X'], 
    'C Y': 0+scores['Y'],
    'C Z': 3+scores['Z']
}

decoded = {
    'A X': outcome['A Z'],
    'A Y': outcome['A X'],
    'A Z': outcome['A Y'],
    'B X': outcome['B X'],
    'B Y': outcome['B Y'],
    'B Z': outcome['B Z'],
    'C X': outcome['C Y'], 
    'C Y': outcome['C Z'],
    'C Z': outcome['C X']
}

total = 0
for i in range(len(moves)):
    total += decoded[moves[i]]

print(total)
