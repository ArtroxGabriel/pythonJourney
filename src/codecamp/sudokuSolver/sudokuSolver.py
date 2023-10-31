def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    # linha
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Coluna
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Quadrante
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def sudoku_solver(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if sudoku_solver(puzzle):
                return True

        puzzle[row][col] = -1

    return False


if __name__ == "__main__":
    eg = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],
        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],
        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1],
    ]
    print(sudoku_solver(eg))
    # {example_board[0][0]}
    print(f'''
        ++=====================================++
        || {eg[0][0]} | {eg[0][1]} | {eg[0][2]} || {eg[0][3]} | {eg[0][4]} | {eg[0][5]} || {eg[0][6]} | {eg[0][7]} | {eg[0][8]} ||  
        || {eg[1][0]} | {eg[1][1]} | {eg[1][2]} || {eg[1][3]} | {eg[1][4]} | {eg[1][5]} || {eg[1][6]} | {eg[1][7]} | {eg[1][8]} ||  
        || {eg[2][0]} | {eg[2][1]} | {eg[2][2]} || {eg[2][3]} | {eg[2][4]} | {eg[2][5]} || {eg[2][6]} | {eg[2][7]} | {eg[2][8]} ||  
        ++=====================================++  
        || {eg[3][0]} | {eg[3][1]} | {eg[3][2]} || {eg[3][3]} | {eg[3][4]} | {eg[3][5]} || {eg[3][6]} | {eg[3][7]} | {eg[3][8]} ||  
        || {eg[4][0]} | {eg[4][1]} | {eg[4][2]} || {eg[4][3]} | {eg[4][4]} | {eg[4][5]} || {eg[4][6]} | {eg[4][7]} | {eg[4][8]} ||  
        || {eg[5][0]} | {eg[5][1]} | {eg[5][2]} || {eg[5][3]} | {eg[5][4]} | {eg[5][5]} || {eg[5][6]} | {eg[5][7]} | {eg[5][8]} ||  
        ++=====================================++
        || {eg[6][0]} | {eg[6][1]} | {eg[6][2]} || {eg[6][3]} | {eg[6][4]} | {eg[6][5]} || {eg[6][6]} | {eg[6][7]} | {eg[6][8]} ||  
        || {eg[7][0]} | {eg[7][1]} | {eg[7][2]} || {eg[7][3]} | {eg[7][4]} | {eg[7][5]} || {eg[7][6]} | {eg[7][7]} | {eg[7][8]} ||  
        || {eg[8][0]} | {eg[8][1]} | {eg[8][2]} || {eg[8][3]} | {eg[8][4]} | {eg[8][5]} || {eg[8][6]} | {eg[8][7]} | {eg[8][8]} ||  
        ++=====================================++
    ''')
