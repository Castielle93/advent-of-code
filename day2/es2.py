# A rock
# B paper
# C scissors

# X lose
# Y draw
# Z win

# shape points
# 1 rock
# 2 paper
# 3 scissors

# win points
# 0 loss
# 3 draw
# 6 win


shapeRock = 1
shapePaper = 2
shapeScissors = 3

lose = 0
draw = 3
win = 6

diz = {('A', 'X'): shapeScissors + lose, ('A', 'Y'): shapeRock + draw, ('A', 'Z'): shapePaper + win,
       ('B', 'X'): shapeRock + lose, ('B', 'Y'): shapePaper + draw, ('B', 'Z'): shapeScissors + win,
       ('C', 'X'): shapePaper + lose, ('C', 'Y'): shapeScissors + draw, ('C', 'Z'): shapeRock + win}
score = 0

with open('input.txt') as infile:
    for a, b in (tuple(elem.strip().split(' ')) for elem in infile.readlines()):
        score += diz[a, b]

print(score)

