import csv


def read_csv_cols(path: str) -> list[list]:
    with open(path, "r", newline="") as file:
        has_header = csv.Sniffer().has_header(file.read(1024))
        file.seek(0)

        reader = csv.reader(file)
        if has_header:
            next(reader)
        columns = [[float(elem) for elem in column] for column in zip(*reader)]

        return columns


def read_csv_rows(path: str) -> list[list]:
    with open(path, "r", newline="") as file:
        has_header = csv.Sniffer().has_header(file.read(1024))
        file.seek(0)

        reader = csv.reader(file)
        if has_header:
            next(reader)
        return [[float(elem) for elem in row] for row in reader]


def write_csv(path: str, data: list[list]) -> None:
    with open(path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


if __name__ == "__main__":
    path = "data/pescados.csv"
    data_rows = read_csv_rows(path)
    data_cols = read_csv_cols(path)
    print(data_rows)
    print(data_cols)
