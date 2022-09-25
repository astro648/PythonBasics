import csv

with open('1wklaunch.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            print("")
            line_count += 1
        else:
            print(f'\t{row[0]} is getting launched on the {row[1]}')
            print("")
            line_count += 1