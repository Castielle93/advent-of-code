# A rock
# B paper
# C scissors

# X rock
# Y paper
# Z scissors

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

diz = {('A', 'X'): shapeRock + draw, ('A', 'Y'): shapePaper + win, ('A', 'Z'): shapeScissors + lose, ('B', 'X'): shapeRock + lose,
       ('B', 'Y'): shapePaper + draw, ('B', 'Z'): shapeScissors + win, ('C', 'X'): shapeRock + win,
       ('C', 'Y'): shapePaper + lose, ('C', 'Z'): shapeScissors + draw}
score = 0

with open('input.txt') as infile:
    for a, b in (tuple(elem.strip().split(' ')) for elem in infile.readlines()):
        score += diz[a, b]

print(score)

