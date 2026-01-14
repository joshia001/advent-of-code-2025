input_file_path = "day4/day4input.txt"
limit = 4

with open(input_file_path) as f:
    grid = [line.rstrip("\n") for line in f]

grid_size = (len(grid), len(grid[0]))

def get_neighbours(row, col, grid_size):
    neighbours = []
    directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
    for d in directions:
        if 0 <= row + d[0] <= grid_size[0]-1 and 0 <= col + d[1] <= grid_size[1]-1:
            neighbours.append((row+d[0], col+d[1]))
    return neighbours

def can_access(neighbours, grid, limit):
    adj_rolls = 0
    for n in neighbours:
        if grid[n[0]][n[1]] == "@":
            adj_rolls += 1
    return adj_rolls < limit
    
def main(grid, grid_size, limit):
    num_can_access = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                neighbours = get_neighbours(row, col, grid_size)
                if can_access(neighbours, grid, limit):
                    num_can_access += 1 

    print(f"Rolls that can be accessed by a forklift: {num_can_access}")
            
if __name__ == '__main__':
    main(grid, grid_size, limit)
        

