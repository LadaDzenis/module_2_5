
def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)

get_matrix(2, 5, 44)
get_matrix(4, 1, 55)
get_matrix(3, 2, 77)



