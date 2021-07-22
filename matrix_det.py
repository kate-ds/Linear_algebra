def my_det(matrix):
    n = len(matrix)
    assert n == len(matrix[0]), 'Matrix dimention error'
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [string[:j] + string[j+1:] for string in (matrix[:0]+matrix[1:])]
            det += matrix[0][j]* (-1)**(j)*my_det(minor)
    return det

def my_det_test():
    a = [[1, -2], [3, 0]]
    b = [[4, -1, 0], [0, 5, 1]]
    c = [[1, 2, 3, 4], [1, 4, 5, 6], [2, 7, 8, 0], [1, 4, 2, 8]]
    d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    e = [[1]]
    print("Test1 -", "OK" if my_det(a) == 6 else "False")
    print("Test2 -", "OK" if my_det(c) == -70 else f"{print(my_det(c))} - False")
    print("Test3 -", "OK" if my_det(d) == 0 else f"{print(my_det(d))} - False")
    try:
        my_det(b)
    except AssertionError:
        print("Test4 - OK")
    print("Test5 -", "OK" if my_det(e) == 1 else "False")

my_det_test()