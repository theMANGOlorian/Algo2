
def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    
    def backtrack(board, i, j):
        # se siano oltre l'ultima riga è finita la matrice
        if i == 9:
            return True
        
        # se siamo  oltre l'ultima colonna allora si va ad una nuova riga
        if j == 9:
            return backtrack(board, i + 1, 0)

        if board[i][j] != ".":
            return backtrack(board, i, j + 1)

        for num in range(1, 10):
            if isValid(board, num, i, j):
                board[i][j] = str(num)
                if backtrack(board, i, j + 1):
                    return True
                board[i][j] = "."

        return False
    
    backtrack(board, 0, 0)
    return board

def isValid(board, num, i, j):
    num = str(num)
    # Verifica la riga e la colonna
    for index in range(9):
        if board[i][index] == num or board[index][j] == num:
            return False


    # Verifica il blocco 3x3
    startRow = 3 * (i // 3)
    startCol = 3 * (j // 3)

    for row in range(startRow, startRow + 3):
        for col in range(startCol, startCol + 3):
            if board[row][col] == num:
                return False

    return True


board = [
    [".",".",".","3","9",".",".",".","."],
    [".","5",".","6",".",".",".",".","9"],
    [".","4",".",".",".","2",".","6","."],
    [".",".","7",".",".","5",".","1","."],
    [".",".","3",".",".",".",".","9","."],
    [".",".","8",".","7","3",".",".","2"],
    [".",".","5",".",".","6","8",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".","1",".",".",".","7",".","2","."]
]

M = solveSudoku(board)
for i in M:
    print(i)
