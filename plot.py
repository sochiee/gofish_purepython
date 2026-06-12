from matplotlib import pyplot as plt
import seaborn as sns

from data import read_csv_cols, read_csv_rows


def plot_aprox(
    x: list[float], aprox: list[float], truth: list[float], name: str, title: str
) -> None:
    plt.figure(figsize=(8, 5))

    sns.scatterplot(x=x, y=truth, linewidth=0, s=75, color="cornflowerblue")
    sns.lineplot(x=x, y=aprox, color="orange")

    plt.xlabel("Volumen (cm$^3$)", fontsize=10)
    plt.ylabel("Peso (kg)", fontsize=10)
    plt.title(title, fontsize=13, pad=15)
    plt.savefig("media/" + name + ".png", dpi=500)
    plt.clf()


def plot_data(x: list[float], y: list[float]) -> None:
    plt.figure(figsize=(8, 5))

    sns.scatterplot(x=x, y=y, linewidth=0, s=75, color="cornflowerblue")
    plt.xlabel("Volumen (cm$^3$)", fontsize=10)
    plt.ylabel("Peso (kg)", fontsize=10)
    plt.title("Relación entre el peso y volumen de los Róbalos", fontsize=13, pad=15)

    plt.savefig("media/pesovolumen.png", dpi=500)
    plt.clf()


if __name__ == "__main__":
    path = "data/aproximaciones.csv"
    long, peso, linear, multilinear = read_csv_rows(path)

    sns.set_theme(style="darkgrid", palette="pastel")

    plot_data(long, peso)
    plot_aprox(long, linear, peso, "linear_aprox", "Aproximación linear")
    plot_aprox(long, multilinear, peso, "multilinear_aprox", "Aproximación polinomica")
