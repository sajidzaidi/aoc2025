from itertools import product 

with open('input.txt', 'r') as f:
    lines = f.readlines()
grid = {x + 1j * y: 1 if val=='@' else 0 for y, line in enumerate(lines)
        for x, val in enumerate(line)}

def neighbors_8(grid, pos):
    candidates = [pos + dx + dy for dx, dy in product([-1, 0, 1], [-1j, 0j, 1j])]
    return [p for p in candidates if p != pos and p in grid]

part1_count=0
for pos in grid.keys():
    if grid[pos]==1:
        part1_count+= sum(grid[x] for x in neighbors_8(grid,pos)) < 4
print(part1_count)

def removable_rolls(grid):
    rolls=0
    for pos in grid.keys():
        if grid[pos]==1:
            rolls+= sum(grid[x] for x in neighbors_8(grid,pos)) < 4
    return rolls

current_rolls=removable_rolls(grid)
total_removed=0
while current_rolls>0:
    points=[]
    for pos in grid.keys():
        if grid[pos]==1 and sum(grid[x] for x in neighbors_8(grid,pos)) < 4:
            points.append(pos)
    for pos in points:
        grid[pos]=0
    total_removed+= current_rolls
    current_rolls = removable_rolls(grid)
print(total_removed)
