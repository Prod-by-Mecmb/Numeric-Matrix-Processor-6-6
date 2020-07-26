import numpy as np

def add_matrix():
    matA = [int(x) for x in input('Enter size of the first matrix: ').split(" ")]
    print('Enter first matrix:')
    A = list([float(x) for x in input().split(" ")] for y in range(matA[0]))
    matB = [int(x) for x in input('Enter size of the second matrix: ').split(" ")]
    print('Enter second matrix:')
    B = list([float(x) for x in input().split(" ")] for y in range(matB[0]))
    if len(A) != len(B):
        return 'The operation cannot be performed.'
    else:
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scalar_mult():
    matA = [int(x) for x in input('Enter size of the matrix: ').split(" ")]
    print('Enter matrix:')
    A = list([float(x) for x in input().split(" ")] for y in range(matA[0]))
    scalar = float(input())
    return [[A[i][j] * scalar for j in range(len(A[0]))] for i in range(len(A))]

def mult_mult():
    matA = [int(x) for x in input('Enter size of the first matrix: ').split(" ")]
    print('Enter first matrix:')
    A = list([float(x) for x in input().split(" ")] for y in range(matA[0]))
    matB = [int(x) for x in input('Enter size of the second matrix: ').split(" ")]
    print('Enter second matrix:')
    B = list([float(x) for x in input().split(" ")] for y in range(matB[0]))
    if matA[1] == matB[0]:
        result = [[0 for i in range(matB[1])] for j in range(matA[0])]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        return 'The operation cannot be performed.'

def create_matrix():
    matA = [int(x) for x in input('Enter size of the matrix: ').split(" ")]
    print('Enter matrix:')
    return list([float(x) for x in input().split(" ")] for y in range(matA[0]))

def transpose():
    xochu_pitsu = int(input('1. Main diagonal\n'
                            '2. Side diagonal\n'
                            '3. Vertical line\n'
                            '4. Horizontal line\n'
                            'Your choice: '))
    if xochu_pitsu == 1:
        A = create_matrix()
        return map(list, zip(*A))
    elif xochu_pitsu == 2:
        A = create_matrix()
        result = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        result2 = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in (range(len(A))):
            for j in range(len(A[0])):
                result[i] = A[i][::-1]

        for i in range(len(result)):
            for j in range(len(result[0])):
                result2[j][i] = result[i][j]

        for i in (range(len(result2))):
            for j in range(len(result2[0])):
                result[i] = result2[i][::-1]
        return result
    elif xochu_pitsu == 3:
        A = create_matrix()
        result = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in (range(len(A))):
            for j in range(len(A[0])):
                result[i] = A[i][::-1]
        return result
    else:
        A = create_matrix()
        return A[::-1]

def printing(K):
    print('The result is:')
    if type(K) == str:
        print(K)
    else:
        for r in K:
            print(*r)

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for j, coef in enumerate(matrix[0]):
            minor = [[matrix[i][k] for k in range(0, len(matrix)) if k != j] for i in range(1, len(matrix))]
            det += ((-1) ** j) * coef * determinant(minor)
        return det

def inverse():
    A = create_matrix()
    A = np.array(A)
    return np.linalg.inv(A)

while True:
    userchoice = int(input('1. Add matrices\n'
                        '2. Multiply matrix by a constant\n'
                        '3. Multiply matrices\n'
                        '4. Transpose matrix\n'
                        '5. Calculate a determinant\n'
                        '6. Inverse matrix\n'
                        '0. Exit\n'
                        'Your choice: '))
    if userchoice == 1:
        K = add_matrix()
        printing(K)
        continue
    if userchoice == 2:
        K = scalar_mult()
        printing(K)
        continue
    if userchoice == 3:
        K = mult_mult()
        printing(K)
        continue
    if userchoice == 4:
        K = transpose()
        printing(K)
        continue
    if userchoice == 5:
        matrix = create_matrix()
        print("The result is:\n{}\n".format(determinant(matrix)))
        continue
    if userchoice == 6:
        K = inverse()
        printing(K)
        continue
    if userchoice == 0:
        exit()