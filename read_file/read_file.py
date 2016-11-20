import csv

def read_file(file):
    with open(file, mode='r') as infile:
        reader = csv.reader(infile)
        # with open('coors_new.csv', mode='w') as outfile:
        #     writer = csv.writer(outfile)
        #     mydict = {rows[0]:rows[1] for rows in reader}
