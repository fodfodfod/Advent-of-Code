file = open("day 1/input.txt", "r")
raw_string = file.read()
file.close()
# elves = []
# for i in range(0, len(raw_string) -1):
#     if(raw_string[i] == "\n" and raw_string[i+1] == "\n"):

elves = raw_string.split("\n\n")
print(len(elves))

biggest_elf = 0
for elf in elves:
    elf_total = 0
    elf_string = elf.split("\n")
    for i in elf_string:
        elf_total += int(i)
    if(elf_total > biggest_elf):
        biggest_elf = elf_total
print(biggest_elf)