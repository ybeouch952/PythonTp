def sum_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Si les dimensions ne correspondent pas, on ne peut pas faire la somme
    
    # Initialiser la matrice de résultat
    result = []
    
    # Parcourir chaque ligne
    for i in range(len(matrix1)):
        # Initialiser une nouvelle ligne pour le résultat
        row_result = []
        # Parcourir chaque élément de la ligne
        for j in range(len(matrix1[0])):
            # Additionner les éléments correspondants des deux matrices
            row_result.append(matrix1[i][j] + matrix2[i][j])
        # Ajouter la ligne à la matrice de résultat
        result.append(row_result)
    
    return result

# Exemple de matrices 3x3
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Calculer la somme des matrices
matrix_sum = sum_matrices(matrix1, matrix2)

# Afficher le résultat
if matrix_sum:
    print("Somme des matrices :")
    for row in matrix_sum:
        print(row)
else:
    print("Les matrices n'ont pas les mêmes dimensions, donc elles ne peuvent pas être additionnées.")