from data import read_csv_cols
from linear_regression import calc_error, olr, pearson
from linalg import linear_solver, transpose

if __name__ == "__main__":
    path = "data/pescados.csv"
    longitudes, pesos, circunferencias = read_csv_cols(path)
    longitudes_cubo = [l**3 for l in longitudes]
    circunferencias_cuadrado = [c**2 for c in circunferencias]
    lc2 = [l * c2 for l, c2 in zip(longitudes, circunferencias_cuadrado)]

    simple_data = [longitudes_cubo, pesos]
    simple_data = transpose(simple_data)

    data = [longitudes_cubo, lc2, pesos]
    data = transpose(data)

    r = pearson(longitudes, pesos)
    print(r)

    beta = olr(simple_data)
    k = beta[0]
    print(k)

    a, b = olr(data)
    print(a, b)

    lineal_aprox = [k * (l**3) for l in longitudes]
    multilineal_aprox = [a * l3i + b * lc2i for l3i, lc2i in zip(longitudes_cubo, lc2)]

    error_lineal = calc_error(lineal_aprox, pesos)
    multilineal_error = calc_error(multilineal_aprox, pesos)

    print(f"error lineal: {error_lineal}")
    print(f"error polinomial: {multilineal_error}")
