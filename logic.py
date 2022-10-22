from score import Score

score = Score()

def compress(mat):
    """returning new compressed matrix and the flag variable."""
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if(mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]
                if(j != pos):
                    changed = True
                pos += 1
    return new_mat, changed

def merge(mat):
    """function to merge the cell in matrix after compressing"""
    changed = False
    for i in range(4):
        for j in range(3):
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
                mat[i][j] = mat[i][j] * 2
                score.score += mat[i][j]
                mat[i][j + 1] = 0
                changed = True
    return mat, changed
 
def reverse(mat):
    """function to reverse the matrix means reversing the content of
        each row (reversing the sequence)"""
    new_mat =[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat
 
def transpose(mat):
    """function to get the transpose of matrix means interchanging rows and column"""
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
 

def move_left(grid):
    """function to update the matrix if we move / swipe left"""
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    return new_grid, changed
 

def move_right(grid):
    """function to update the matrix if we move / swipe right"""
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    """function to update the matrix if we move / 
    swipe up to move up we just take transpose of matrix"""
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed
 

def move_down(grid):
    """function to update the matrix if we move / 
    swipe down to move down we take transpose"""
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def Exists_horizontalMoves(mat):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1]:
                return True
    return False

def Exists_verticalMoves(mat):
    for i in range(3):
        for j in range(4):
            if mat[i][j] == mat[i + 1][j]:
                return True
    return False

