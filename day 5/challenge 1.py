file = open("day 5/input.txt", "r")
raw_string = file.read()
file.close()

def parse_command(command):
    args = command.split(" ")
    number = int(args[1])
    start = int(args[3])
    end = int(args[5])
    stacks_of_crates_because_the_crates_are_in_stacks[end].append(stacks_of_crates_because_the_crates_are_in_stacks[start][:number])
    

stack_string = raw_string.split("\n\n")[0]
commands = raw_string.split("\n\n")[1]
line_strings = stack_string.split("\n")

num_stacks = int((len(line_strings[0])+1)/4)
stacks_of_crates_because_the_crates_are_in_stacks = []

for i in range(num_stacks):
    stacks_of_crates_because_the_crates_are_in_stacks.append([])
    for line in line_strings[:-1]:
        letter = line[4*i+1]
        if letter != " ":
            stacks_of_crates_because_the_crates_are_in_stacks[i].append(letter)
    stacks_of_crates_because_the_crates_are_in_stacks[i] = stacks_of_crates_because_the_crates_are_in_stacks[i][::-1]

for command in commands.split("\n")[:-1]:
    parse_command(command)