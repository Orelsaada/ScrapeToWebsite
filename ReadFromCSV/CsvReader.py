import csv
import datetime
import os
from Scraper.BugScraper import filepath

def readCSV(path):
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            columns_titles = line
            columns_number = len(line)
            break

        all_columns_list = []
        rows_number = 0
        for line in csv_reader:
            all_columns_list.append(line)
            rows_number += 1
    print('ReadFromCSV Worked!')
    # CSV creation time (Adding 3 hours because of heroku timezone)
    timestamp = os.path.getctime(filepath)
    creation_time = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(hours=3)
    creation_time = creation_time.strftime("%d/%m/%Y \n%H:%M")
    return columns_titles, all_columns_list, columns_number, rows_number, creation_time
    # print(f'Titles: {columns_titles}\nColumns Number: {columns_number}\nRows Number: {rows_number}')
    # print(all_columns_list)


if __name__ == '__main__':
    readCSV()