
f = open("Input.txt", "r")
lines = f.readlines()
values = [int(x) for x in lines]
index = 0
step = 0
while index >= 0 and index < len(values):
	pIndex = index
	offset = values[index] 
	index = offset + index
	if offset < 3:
		values[pIndex] = values[pIndex] + 1
	else:
		values[pIndex] = values[pIndex] - 1
	step = step + 1

print("Part 1 Answer: " + str(step))

