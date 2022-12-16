file = open("day 3/input.txt", "r")
raw_string = file.read()
file.close()


def score_letter(letter):
    if(letter.islower()):
        return ord(letter) - 96
    else:
        return ord(letter) - 38
lines = raw_string.split("\n")
print(len(lines))
total_score = 0
for i in range(0, len(lines), 3):
    line = lines[i]
    print(i)
    for letter in line:
        if letter in lines[i+1] and letter in lines[i+2]:
            total_score += score_letter(letter)
            break    
print(total_score)


    