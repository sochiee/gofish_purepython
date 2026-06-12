from linalg import matmul, matrix_to_str, matvec, qr, transpose


def olr(data: list[list]) -> list[float]:
    """
    Dada una lista con observaciones, regresa una lista de variables explanatorias.
    Para cada una de las observaciones, el ultimo elemento debe ser el escalar respuesta
    """
    n = len(data)
    m = len(data[0])

    regressors = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m - 1):
            regressors[i].append(data[i][j])

    response = [data[i][m - 1] for i in range(n)]

    q, r = qr(regressors)
    qt = transpose(q)
    qty = matvec(qt, response)

    k = len(r)

    explanatory_vars = [0.0] * k

    for i in range(k - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, k):
            sum += r[i][j] * explanatory_vars[j]
        explanatory_vars[i] = (qty[i] - sum) / r[i][i]

    return explanatory_vars


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(olr(A))
