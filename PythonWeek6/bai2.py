def transposition(matrix):
    '''
    param matrix: a 2D list
    return: the transposed matrix

    '''
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix

n,m = map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
trans = transposition(matrix)

#unpacking list
for i in trans:
    for j in i:
        print(j,end=" ")
    print()



