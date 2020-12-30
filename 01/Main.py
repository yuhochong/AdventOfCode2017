
f = open("Input.txt", "r")
lines = f.readlines()
for l in lines:
	sum = 0
	count = len(l)
	for i in range(0, count):
		if l[i] == l[(i + 1) % count]:
			sum += int(l[i])
	print("Part 1 Answer: " + str(sum))

	sum = 0
	half = int(len(l) / 2)
	for i in range(0, count):
		if l[i] == l[(i + half) % count]:
			sum += int(l[i])
	print("Part 2 Answer: " + str(sum))