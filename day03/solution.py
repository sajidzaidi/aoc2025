
def recursive(remaining_string,remaining_digits=12):
    if remaining_digits>1:
        eligible_string=remaining_string[:-(remaining_digits-1)]
    else:
        eligible_string=remaining_string
    start=eligible_string.index(max(eligible_string))+1
    remaining_string = remaining_string[start:]
    if remaining_digits>1:
        return max(eligible_string) + recursive(remaining_string,remaining_digits-1)
    else:
        return max(eligible_string)
test_case = '234234234234278'


with open('input.txt', 'r') as f:
    lines = f.readlines()
total=0
part2_total=0
for line in lines:
    
    # Remove newline characters and split the line
    line = line.strip()
    line_length = len(line)
    highest_tens=0
    highest_ones=0
    for t, ten in enumerate(line[:-1]):
        if int(ten)<highest_tens:
            continue
        for one in line[t+1:]:
            if int(ten)>highest_tens or int(one)>highest_ones:
                highest_tens=int(ten)
                highest_ones=int(one)
    

    total+= 10*highest_tens + highest_ones
    part2_total+=int(recursive(line))
print(total)
print(part2_total)


