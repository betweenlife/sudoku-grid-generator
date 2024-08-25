import random
import openpyxl

def is_safe(grid, row, col, num):
    # row check
    if num in grid[row]:
        return False
    # column check
    for i in range(9):
        if grid[i][col] == num:
            return False
    # 3x3 block check
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(grid):
    row, col = find_empty_cell(grid)
    # no empty cell -> grid completed
    if row is None and col is None:
        return True
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for num in numbers:
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            # backtrack
            grid[row][col] = 0
    return False

def generate_sudoku_grid():
    grid = [[0 for i in range(9)] for i in range(9)] # empty grid
    solve_sudoku(grid)
    return grid

def check_at_least_2_element_block(grid, row, col):
    counter = 0
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] != 0:
                counter += 1
    return True if counter >= 3 else False

def remove_numbers(grid, num_cells_to_remove):
    attempts = num_cells_to_remove
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while grid[row][col] == 0 or not check_at_least_2_element_block(grid, row, col):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        grid[row][col] = 0
        attempts -= 1
    return grid

def get_difficolty_choice(not_valid=False):
    message = "Enter your number: "
    if not_valid:
        message = "Not valid number! " + message
    try:
        choice = int(input(message))
        while choice not in [1, 2, 3]:
            return get_difficolty_choice(not_valid)
        return choice
    except Exception:
        return get_difficolty_choice(not_valid)


grid = generate_sudoku_grid() 

print('DIFFICULTY OF THE GRID\n')
print('1 - Easy')
print('2 - Medium')
print('3 - Hard\n\n')
   
choice = get_difficolty_choice()

if choice == 1:
    grid = remove_numbers(grid, 30)  # keep 51 cells filled
elif choice == 2:
    grid = remove_numbers(grid, 40)  # keep 41 cells filled
else:
    grid = remove_numbers(grid, 50)  # keep 31 cells filled
    
workbook = openpyxl.load_workbook("sudoku.xlsx")
sheet = workbook.active
for i in range(9):
    for j in range(9):
        value = grid[i][j]
        sheet.cell(row=i+1, column=j+1).value = "" if value == 0 else value
workbook.save("sudoku.xlsx")
print(f"Sudoku grid saved into sudoku.xlsx file!")
        




    




