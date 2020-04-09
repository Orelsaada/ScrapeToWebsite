from flask import Flask, render_template
from ReadFromCSV.CsvReader import readCSV
from Scraper.BugScraper import scrape
import os

app = Flask(__name__)


@app.route("/")
def index():

    # Make sure there is a CSV file.
    path = os.getcwd()
    ReadFromCSV_path = os.path.join(path, 'ReadFromCSV')
    BugData_path = os.path.join(ReadFromCSV_path, 'BugData.csv')
    ReadFromCSV_files = os.listdir(ReadFromCSV_path)
    if 'BugData.csv' not in ReadFromCSV_files:
        scrape()

    creation_time = scrape()
    columns_titles, all_columns_list, columns_number, rows_number = readCSV(BugData_path)
    return render_template("index.html", columns_titles=columns_titles,
                           all_columns_list=all_columns_list,
                           columns_number=columns_number, rows_number=rows_number,
                           creation_time=creation_time)


if __name__ == '__main__':
    app.run(debug=True)


