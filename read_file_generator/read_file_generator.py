import csv

def get_data(filename, delimiter):
    with open(filename, "rt") as csvfile:
        datareader = csv.reader(csvfile, delimiter=delimiter)
        for row in datareader:
            yield row

def create_dict_from_list(row, row_titles):
    data = {}
    for idx, row_title in enumerate(row_titles):
        data[row_title] = row[idx]

    return data

# name, age, start_year, current_positions = [(row.text).strip() for row in rows]
