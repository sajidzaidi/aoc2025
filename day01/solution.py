# Read lines from input.txt and split them
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Process each line: strip whitespace and split
split_lines = []
for line in lines:
    # Remove newline characters and split the line
    line = line.strip()
    if line:  # Only process non-empty lines
        # Split the direction from the number (e.g., "R30" -> ["R", "30"])
        direction = line[0]
        number = line[1:]
        split_lines.append((direction, number))

# Print the results
current_number = 50
zero_count = 0
for direction, number in split_lines:
    number = int(number)  # Convert string to integer
    if direction == "R":
        current_number = (current_number + number) % 100
    elif direction == "L":
        current_number = (current_number - number) % 100
    if current_number == 0:
        zero_count += 1
print(f"Number of zeros: {zero_count}")

