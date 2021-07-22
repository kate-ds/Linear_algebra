def matrix_multiply(matrix1, matrix2):
    n = len(matrix1)
    m = len(matrix2[0])
    mult = [[0 for i in range(n)] for i in range(m)]
    print(mult)
    for i in range(n):
      for j in range(m):
        for k in range(len(matrix2)):
           mult[i][j] += matrix1[i][k] * matrix2[k][j]
    print(mult)
    return mult

def matrix_multiply_test():
    a = [[1, -2], [3, 0]]
    b = [[4, -1], [0, 5]]
    c = [[1, 2, 3], [4, 5, 6]]
    d = [[1, 2], [3, 4], [5, 6]]
    print("Test1 - ", "OK" if matrix_multiply(a, b) == [[ 4, -11], [ 12,  -3]] else "False")
    print("Test2 - ", "OK" if matrix_multiply(c, d) == [[22, 28], [49, 64]] else "False")

matrix_multiply_test()
