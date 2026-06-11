def dot(x: list[float], y: list[float]) -> float:
    """Producto punto entre dos vectores x, y"""
    return sum(xi + yi for xi, yi in zip(x, y))


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
