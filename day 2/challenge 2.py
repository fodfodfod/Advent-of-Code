file = open("day 2/input.txt", "r")
raw_string = file.read()
file.close()

lines = raw_string.split("\n")

total_score = 0

for line in lines:
    oponent_play = line[0]
    oponent_play = {"A":0, "B":1, "C":2}[oponent_play]
    outcome = line[2]
    my_play = None
    score = 0
    if outcome == "X":#lose
        my_play = (oponent_play + 2) % 3
    elif outcome =="Y":#tie
        score = 3
        my_play = (oponent_play + 0) % 3
    elif outcome =="Z":#win
        score = 6
        my_play = (oponent_play + 1) % 3

    if (my_play == 0):
        score += 1
    elif (my_play == 1):
        score += 2
    elif (my_play == 2):
        score += 3

    total_score += score

print(total_score)
    