def movimento_valido(grid,linha,coluna,numero):
    for x in range(9):
        if grid[linha][x] == numero:
            return False
    for x in range(9):
        if grid[x][coluna] ==  numero:
            return False

    canto_linha = linha - linha % 3
    canto_coluna = coluna - coluna % 3
    for x in range(3):
        for y in range(3):
            if grid[canto_linha + x][canto_coluna + y]  == numero:
                return False
    return True        



def resolver(grid,linha,coluna):

    if coluna == 9:
        if linha == 8:
            return True
        linha += 1
        coluna = 0

    if grid[linha][coluna] > 0:
        return resolver(grid,linha, coluna + 1)

    for num in range(1,10):
        if movimento_valido(grid,linha,coluna,num):

            grid[linha][coluna] = num

            if resolver(grid,linha,coluna + 1):
                return True
        grid[linha][coluna] = 0
    return False


sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if resolver(sudoku_grid,0,0):
    for i in range(9):
        for j in range(9):
            print(sudoku_grid[i][j], end=" ")
        print()
else:
    print('sem solucao')        
