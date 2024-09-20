









grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]


row = 0
column = 0

columns = []
for row in range(len(grid[0])):
    temp = []
    for col in range(len(grid)):
        temp.append(grid[col][row])
    columns.append(tuple(temp))

print(columns)