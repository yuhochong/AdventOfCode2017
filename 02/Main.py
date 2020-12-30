
f = open("Input.txt", "r")
lines = f.readlines()

sum = 0
for l in lines:
	values = [int(x) for x in l.split('\t')]
	minVal = min(values)
	maxVal = max(values)
	sum += maxVal - minVal
print("Part 1 Answer: " + str(sum))

sum = 0
for l in lines:
	values = [int(x) for x in l.split('\t')]
	for i in range(0, len(values) - 1):
		for j in range(i+1, len(values)):
				minVal = min(values[i], values[j])
				maxVal = max(values[i], values[j])
				if(maxVal % minVal == 0):
					sum += int(maxVal / minVal)
print("Part 2 Answer: " + str(sum))

