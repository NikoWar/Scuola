import random

dim = 5

mat = [[0]*dim]*dim

for r in range(dim):
    for c in range(dim):
        if not r==c:
            mat[r][c] =int(random.random()*10)
            mat[c][r] = mat[r][c]

print(mat)