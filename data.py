import csv


def read_csv(path: str) -> list[list]:
    with open(path, "r", newline="") as file:
        has_header = csv.Sniffer().has_header(file.read(1024))
        file.seek(0)

        reader = csv.reader(file)
        if has_header:
            next(reader)
        columns = [[float(elem) for elem in column] for column in zip(*reader)]

        return columns


if __name__ == "__main__":
    path = "data/pescados.csv"
    data = read_csv(path)
    print(data)
