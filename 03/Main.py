input = 361527

r = 1
while True:
    if r*r >= input:
        # max would be r - 1 distance
        # if r is odd max is r-1, min is (r-1)/2
        # if r is even max is r, min is r/2
        if r % 2 == 0:
            dMax = r
        else:
            dMax = r - 1
        mid = (r-1)**2 + r
        ans = dMax - int(abs(input - mid))
        break;
    r += 1

print("Part 1 Answer: " + str(ans))

size = 1000
grid=[]
for i in range(0, size):
    row = [0] * size
    grid.append(row)

x = int(size / 2)
y = int(size / 2)
dx = int(1)
dy =  int(0)
grid[x][y] = 1

while True:
    sum = 0
    x = x + dx
    y = y + dy
    # for each neighbor including diagonal, sum up value.
    for combo in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]:
        sum += grid[x + combo[0]][y + combo[1]]

    grid[x][y] = sum
    if sum > input:
        break
    if dx == 1:
        if grid[x][y-1] == 0:
            dy = -1
            dx = 0
    elif dx == -1:
        if grid[x][y+1] == 0:
            dy = 1
            dx = 0
    elif dy == 1:
        if grid[x+1][y] == 0:
            dy = 0
            dx = 1
    elif dy == -1:
        if grid[x-1][y] == 0:
            dy = 0
            dx = -1

print("Part 2 Answer: " + str(sum))

