def sparse_repr(matrix, dim):
    sparse = dict()
    for i in range(dim[0]):
        for j in range(dim[1]):
            if matrix[i][j] != 0:
                sparse[(i, j)] = matrix[i][j]
    return sparse


def dim(matrix):
    return len(matrix), len(matrix[0])


def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    dim_a = dim(matrix_a)
    dim_b = dim(matrix_b)

    if dim_a[1] != dim_b[0]:
        return [[]]

    sparse_a = sparse_repr(matrix_a, dim_a)
    sparse_b = sparse_repr(matrix_b, dim_b)

    result = [[0 for _ in range(dim_b[1])] for _ in range(dim_a[0])]

    for i in range(dim_a[0]):
        for j in range(dim_b[1]):
            for k in range(dim_a[1]):
                try:
                    result[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
                except KeyError:
                    continue

    return result
