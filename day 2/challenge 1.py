file = open("day 2/input.txt", "r")
raw_string = file.read()
file.close()

lines = raw_string.split("\n")

total_score = 0

for line in lines:
    oponent_play = line[0]
    #convert oponent_play to the same standard
    oponent_play = {"A":"X", "B":"Y", "C":"Z"}[oponent_play]
    my_play = line[2]
    score = 0
    if my_play == "X":#Rock
        score = 1
    elif my_play =="Y":#paper
        score = 2
    elif my_play =="Z":#sisors
        score = 3

    if (my_play == oponent_play):
        score += 3
    elif (my_play == "X" and oponent_play == "Z"):
        score += 6
    elif (my_play == "Y" and oponent_play == "X"):
        score += 6
    elif (my_play == "Z" and oponent_play == "Y"):
        score += 6
    total_score += score

print(total_score)
    