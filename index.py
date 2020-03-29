from flask import Flask, render_template
from ReadFromCSV.CsvReader import readCSV
from main import mainLoop

app = Flask(__name__)


@app.route("/")
def index():
    columns_titles, all_columns_list, columns_number, rows_number = readCSV()
    return render_template("index.html", columns_titles=columns_titles,
                           all_columns_list=all_columns_list,
                           columns_number=columns_number, rows_number=rows_number)
    # return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)


