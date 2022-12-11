file = open("day 3/input.txt", "r")
raw_string = file.read()
file.close()


def score_letter(letter):
    if(letter.islower()):
        return ord(letter) - 96
    elif(letter.isupper()):
        return ord(letter) - 38
    else:
        print("sad")

lines = raw_string.split("\n")
total_score = 0
for line in lines:
    first_section = line[:int(len(line)/2)]
    second_section = line[int(len(line)/2):]
    for letter in first_section:
        if (letter in second_section):
            #score letter
            total_score += score_letter(letter)
            break
print(total_score)


    