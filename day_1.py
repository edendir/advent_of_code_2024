with open("/input_text/day_1.txt") as f:
    inp = f.read()

total_distance = 0
left_list = []
right_list = []
for line in inp:
    line.split()
    left_list[line] = line[0]
    right_list[line] = line[1]

left_list = left_list.sort()
right_list = right_list.sort()

for i in left_list:
    distance = abs(left_list[i] - right_list[i])
    total_distance += distance

print(total_distance)
