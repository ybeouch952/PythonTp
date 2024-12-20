def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None  
    
    result = []
    
    for i in range(len(matrix1)):
        row_result = []  
        for j in range(len(matrix2[0])):  
            for k in range(len(matrix2)):  
                row_result.append(matrix1[i][j] * matrix2[i][j])
        result.append(row_result)
    return result

matrix1 = [
    [1, 0, 2],
    [-1, 3, 1],
    [2, 2, 1]
]

matrix2 = [
    [3, 1, 4],
    [2, 0, 1],
    [0, 1, 5]
]

matrix_product = multiply_matrices(matrix1, matrix2)

if matrix_product:
    print("Matrice produit :")
    for row in matrix_product:
        print(row)
else:
    print("Les matrices ne peuvent pas être multipliées, leurs dimensions ne sont pas compatibles.")
