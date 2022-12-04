file = open("day 1/input.txt", "r")
raw_string = file.read()
file.close()
# elves = []
# for i in range(0, len(raw_string) -1):
#     if(raw_string[i] == "\n" and raw_string[i+1] == "\n"):

elves = raw_string.split("\n\n")
print(len(elves))

elves_total = []
for elf in elves:
    elf_total = 0
    elf_string = elf.split("\n")
    for i in elf_string:
        elf_total += int(i)
    elves_total.append(elf_total)

output = 0
elves_total.sort()
elves_total.reverse()
for elf in elves_total[:3]:
    output += elf
print(output)