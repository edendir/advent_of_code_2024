with open("./input_text/day_2.txt") as f:
    inp = f.read()

lines = inp.splitlines()
safe_count = 0

def is_safe(x):
    differences = [x[i+1] - x[i] for i in range(len(x) - 1)]
    if (all(j < 0 and j in range(-3, 0) for j in differences) or
        all(j > 0 and j in range(1, 4) for j in differences)):
        return True
    else:
        return False
        

for line in lines:
    nums = [int(num.strip()) for num in line.split()]
    if is_safe(nums):
        safe_count += 1
    else:
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            if is_safe(temp):
                safe_count += 1
                break

print(safe_count)
