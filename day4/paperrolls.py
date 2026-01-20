import sys
sys.setrecursionlimit(10000)

input_file_path = "day4/day4input.txt"
limit = 4

with open(input_file_path) as f:
    grid = [line.rstrip("\n") for line in f]

grid_size = (len(grid), len(grid[0]))
print(grid_size)

def get_neighbours(row, col):
    neighbours = []
    directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    for d in directions:
        if 0 <= row + d[0] <= grid_size[0]-1 and 0 <= col + d[1] <= grid_size[1]-1:
            neighbours.append((row+d[0], col+d[1]))
    return neighbours

def can_access(neighbours, removed):
    adj_rolls = 0
    for n in neighbours:
        if grid[n[0]][n[1]] == "@" and not n in removed:
            adj_rolls += 1
    return adj_rolls < limit

def dfs(row, col, removed, visited):
    visited.add((row, col))
    neighbours = get_neighbours(row, col)
    if can_access(neighbours, removed):
            removed.add((row, col))
            for n in neighbours:
                if grid[n[0]][n[1]] == "@":
                    if not (n[0], n[1]) in visited:
                        dfs(n[0], n[1], removed, visited)

                
def main():
    # num_can_access = 0
    removed = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                neighbours = get_neighbours(row, col)
                if can_access(neighbours, removed):
                    # removed.add((row, col))
                    visited = set()
                    dfs(row, col, removed, visited)

    print(f"Rolls that can be accessed by a forklift: {len(removed)}")
            
if __name__ == '__main__':
    main()
        

