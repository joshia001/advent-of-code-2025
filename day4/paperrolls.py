from collections import deque

input_file_path = "day4/day4input.txt"
limit = 4

with open(input_file_path) as f:
    grid = [line.rstrip("\n") for line in f]

grid_size = (len(grid), len(grid[0]))

def get_neighbours(row, col):
    neighbours = set()
    directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    for d in directions:
        if 0 <= row + d[0] <= grid_size[0]-1 and 0 <= col + d[1] <= grid_size[1]-1:
            if grid[row + d[0]][col + d[1]] == "@":
                neighbours.add((row+d[0], col+d[1]))
    return neighbours

def num_adj_rolls(neighbours):
    adj_rolls = 0
    for n in neighbours:
        if grid[n[0]][n[1]] == "@":
            adj_rolls += 1
    return adj_rolls

def main():
    num_can_remove = 0
    rolls_map = {}
    queue = deque([])
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                neighbours = get_neighbours(row, col)
                adj_rolls = len(neighbours)
                if adj_rolls < 4:
                    queue.append(neighbours)
                else:
                    rolls_map[(row, col)] = adj_rolls
  
    while queue:
        res = queue.popleft()
        num_can_remove += 1
        for coord in res:
            if coord in rolls_map:
                rolls_map[coord] -= 1
                if rolls_map[coord] < 4:
                    neighbours = get_neighbours(coord[0], coord[1])
                    queue.append(neighbours)
                    del rolls_map[coord]
                        
    print(f"Rolls that can be accessed by a forklift: {num_can_remove}")
            
if __name__ == '__main__':
    main()