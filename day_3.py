import re

with open("./input_text/day_3.txt") as f:
    inp = f.read()

# Define regex pattern for {mul(x,y)}, do(), and don't()}
pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")

# Find all matches
matches = pattern.findall(inp)
print(matches)

# Setup math variable
math = 0
# set execute variable
execute = True

# Iterate over matches
for match in matches:
    # Check if "do()" in match
    if "do()" in match:
        # Set execute to True
        execute = True
    elif "mul" in match:
        if execute == True:
            # Extract x and y values
            x, y = map(int, re.findall(r"\d+", match))
            # Replace match with x*y
            math += x * y
    elif "don't()" in match:
        # Set execute to False
        execute = False

print(math)
