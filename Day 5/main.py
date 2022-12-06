with open("Day 5/input.txt", "r") as file:
    stacks_raw = file.read().split('\n')

with open("Day 5/input2.txt", "r") as file:
    moves = file.read().split('\n')

for i in range(len(moves)):
    moves[i] = moves[i].replace('move', '').replace('to', '').replace('from', '').split()

stacks = {}
cols = int((len(stacks_raw[0])+1)/4) # Gets number of columns 
for x in range(cols):
    stacks[x+1] = []

for i in stacks: # colums
    for j in range(len(stacks_raw)): # rows
        if stacks_raw[j][(4*(i)-3)] != ' ':
            stacks[i].append(stacks_raw[j][(4*(i)-3)]) # put them into columns rather than rows

for i in stacks:
    stacks[i] = stacks[i][::-1] # Reverse all the lists

for i in range(len(moves)): # Now make the moves [number, from, to]
    for j in range(int(moves[i][0])): # How many to move
        From = int(moves[i][1])
        To = int(moves[i][2])

        stacks[To].append(stacks[From][-1])
        stacks[From].pop(-1)

top_boxes = []
for i in stacks:
    top_boxes.append(stacks[i][-1])

print(''.join(top_boxes))