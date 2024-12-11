def matrix_print(matrix: list[list[str]]) -> None:
    for row in matrix:
        print(', '.join([str(r) for r in row]))


def retrieve_matrix(size: int) -> list[list[int]]:
    matrix = []
    print('\nEscribe los elementos de la matriz binaria separados por comas sin espacios. eg: 0,0,1,0,0\n')  # noqa: E501
    for i in range(size):
        row = [int(x) for x in input(f'Escribe la fila {i + 1} de la matriz: ').split(',')]  # noqa: E501
        if len(row) != size:
            raise Exception(f'La fila no puede ser mas grande de {size}')
        matrix.append(row)
    return matrix


def is_simetric(matrix: list[list[int]], size: int) -> bool:
    simetric = True
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return simetric


def is_anti_simetric(matrix: list[list[int]], size: int) -> bool:
    anti_simetric = True
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != -matrix[j][i]:
                return False
    return anti_simetric


def is_reflexive(matrix: list[list[int]], size: int) -> bool:
    reflexive = True
    for i in range(size):
        if matrix[i][i] != 1:
            return False
    return reflexive


def find_relations(matrix: list[list[int]], size: int) -> bool:
    relations = set()
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                relations.add((i, j))
    return relations


def is_transitive(matrix: list[list[int]], size: int) -> bool:
    # a,b - b,c - a,c
    relations = find_relations(matrix, size)

    if not relations:
        return False

    for a, b in relations:
        if a == b:
            continue

        bc = [r for r in relations if r[0] == b]

        if not bc:
            # not bc relation found in the matrix
            return False

        for _, c in bc:
            if (a, c) in relations:
                break
        else:
            # not ac relation found in the matrix
            return False
    return True


def display_menu():
    try:
        matrix_size = int(input('Escribe el tamaño de la matriz nxn: '))
        matrix = retrieve_matrix(matrix_size)
        print('\nEvaluando la matriz:\n')
        matrix_print(matrix)
        print()

        print(f'La matriz{" " if is_simetric(matrix, matrix_size) else " no "}es simétrica')  # noqa: E501
        print(f'La matriz{" " if is_anti_simetric(matrix, matrix_size) else " no "}es antisimétrica')  # noqa: E501
        print(f'La matriz{" " if is_reflexive(matrix, matrix_size) else " no "}es reflexiva')  # noqa: E501
        print(f'La matriz{" " if is_transitive(matrix, matrix_size) else " no "}es transitiva')  # noqa: E501
    except ValueError:
        print('\nValor ingresado incorrecto. Debes introducir un tamaño de matriz entero y una matriz binaria de 1 y 0\n')  # noqa: E501
        display_menu()


if __name__ == '__main__':
    display_menu()
