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


def calc_error(pred: list[float], truth: list[float]) -> float:
    """Calcula el error entre la predicción y los datos"""
    n = len(pred)
    error = sum([(p - t) ** 2 for p, t in zip(pred, truth)]) / n
    return error


def pearson(regressors: list[float], response: list[float]) -> float:
    """Calcula el coeficiente de Pearson"""
    n = len(regressors)

    suma_x = sum(regressors)
    suma_y = sum(response)
    suma_x2 = sum([xi**2 for xi in regressors])
    suma_y2 = sum([yi**2 for yi in response])
    suma_xy = sum([xi * yi for xi, yi in zip(regressors, response)])

    num = (n * suma_xy) - (suma_x * suma_y)
    den = ((n * suma_x2 - suma_x**2) * (n * suma_y2 - suma_y**2)) ** 0.5

    coef = num / den

    return coef


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(olr(A))
