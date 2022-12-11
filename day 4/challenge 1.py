file = open("day 4/input.txt", "r")
raw_string = file.read()
file.close()


pairs = raw_string.split("\n")
x = 0
for pair in pairs:
    raw_elves = pair.split(",")
    elves = []
    for elf in raw_elves:
        elves.append(elf.split("-"))

    if((int(elves[0][0]) >= int(elves[1][0])) and (int(elves[0][1]) <= int(elves[1][1]))):
        x+=1

    elif((int(elves[1][0]) >= int(elves[0][0])) and (int(elves[1][1]) <= int(elves[0][1]))):
        x+=1 
print(x)