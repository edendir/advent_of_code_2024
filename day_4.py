with open("./input_text/day_4.txt") as f:
    inp = f.read()

xmas_counter = 0

lines = inp.splitlines()

def count_xmas(line):
    count = 0
    for i in range(len(line)-3):
        if line[i:i+4] == "xmas" or line[i:i+4][::-1] == "xmas":
            count += 1 
    return count

def get_diagonals(lines):
    diagonals = []
    rows, cols = len(lines), len(lines[0])

    # Top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diagonal = ''.join(lines[i][d - i] for i in range(max(0, d - cols + 1), min(d + 1, rows)))
        diagonals.append(diagonal)

    # Top-right to bottom-left diagonals
    for d in range(rows + cols - 1):
        diagonal = ''.join(lines[i][cols - 1 - (d - i)] for i in range(max(0, d - cols + 1), min(d + 1, rows)))
        diagonals.append(diagonal)

    return diagonals

# Count occurrences of "xmas" horizontally
for line in lines:
    xmas_counter += count_xmas(line)

# Count occurrences of "xmas" vertically
for col in range(len(lines[0])):
    column = ''.join(line[col] for line in lines)
    xmas_counter += count_xmas(column)

# Count diagonally
diagonals = get_diagonals(lines)
for diagonal in diagonals:
    xmas_counter += count_xmas(diagonal)

# Print the total count of "xmas" in the input text
print(xmas_counter)