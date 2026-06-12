def dot(x: list[float], y: list[float]) -> float:
    """Producto punto entre dos vectores x, y"""
    return sum(xi * yi for xi, yi in zip(x, y))


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """Transpuesta de una matriz"""
    return [list(row) for row in zip(*matrix)]


def matmul(
    matrix_a: list[list[float]], matrix_b: list[list[float]]
) -> list[list[float]]:
    """Multiplicacion AB de dos matrices A y B"""
    transpose_b = transpose(matrix_b)
    return [[dot(row, col) for col in transpose_b] for row in matrix_a]


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Multiplicación de una matriz A por un vector v"""
    return [dot(row, vector) for row in matrix]


def norm(vector: list[float]) -> float:
    """Norma de un vector"""
    return dot(vector, vector) ** 0.5


def proj(vector_u: list[float], vector_v: list[float]) -> list[float]:
    """Calcula proyección de un vector u sobre otro vector v"""
    escalar = dot(vector_u, vector_v) / dot(vector_v, vector_v)
    return [escalar * vi for vi in vector_v]


def normalize(vector_v: list[float]) -> list[float]:
    """Normaliza un vector v"""
    return [vi / norm(vector_v) for vi in vector_v]


def gram_schmidt(column_vecs: list[list[float]]) -> list[list[float]]:
    """Aplica Gram-Schmidt a una lista de vectores"""
    orthogonal_u = []

    for vector in column_vecs:
        u = vector

        for u_k in orthogonal_u:
            p = proj(vector, u_k)
            u = [ui - pi for ui, pi in zip(u, p)]

        orthogonal_u.append(u)

    orthonormal_e = [normalize(u) for u in orthogonal_u]

    return orthonormal_e


def qr(matrix: list[list[float]]) -> list[list[list[float]]]:
    """Descomposición QR de una matriz usando el metodo de Gram-Schmidt"""
    columnas = transpose(matrix)
    orthonormal_cols = gram_schmidt(columnas)

    q = transpose(orthonormal_cols)
    qt = transpose(q)

    r = matmul(qt, matrix)

    no_cols_r = len(r)
    no_rows_r = len(r[0])

    for i in range(no_rows_r):
        for j in range(no_cols_r):
            if r[i][j] <= 1e-10 and j < i:
                r[i][j] = 0.0

    return [q, r]


def linear_solver(
    coef_matrix: list[list[float]], con_vector: list[float]
) -> list[float]:
    """Resuelve un sistema de ecuaciones lineales de la forma Ax=b"""
    n = len(coef_matrix[0])

    q, r = qr(coef_matrix)
    qt = transpose(q)
    qtb = matvec(qt, con_vector)[:n]

    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, n):
            sum += r[i][j] * x[j]
        x[i] = (qtb[i] - sum) / r[i][i]

    return x


def matrix_to_str(matrix: list[list[float]]) -> str:
    """Convierte una matriz a texto formateado con columnas alineadas."""
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return "\n".join(table)


if __name__ == "__main__":
    A = [[1, 4, 7], [2, 5, 8]]
    q, r = qr(A)
    print(matrix_to_str(r))
