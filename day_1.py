with open("./input_text/day_1.txt") as f:
    inp = f.read()

total_distance = 0
left_list = []
right_list = []

line_count = 0
lines = inp.splitlines()
#print(inp)

for line in lines:
    line = line.split()
    left_list.append(line[0])
    right_list.append(line[1])

#print(left_list)
    
left_list = sorted(left_list)
right_list = sorted(right_list)

#print(left_list)

for i in range(len(left_list)):
    distance = abs(int(left_list[i]) - int(right_list[i]))
    total_distance += distance

print(total_distance)

similarity_score = 0
for i in range(len(left_list)):
    similarity_multiplier = right_list.count(left_list[i])
    similarity_score += (int(left_list[i]) * similarity_multiplier)

print(similarity_score)