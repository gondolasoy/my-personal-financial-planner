from flask import Flask, render_template, request
import csv
from calculation import FinancialCalculator

app = Flask(__name__)

result = None
calculator = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'number' in request.form:
            number = int(request.form['number'])
            global calculator
            calculator = FinancialCalculator(number)
            global result
            result = calculator.calculate()

        gotcha_data = request.form.get('gotcha_data')  # Get "Gotcha!" data

        # Check if "Gotcha!" button was clicked and store data in CSV
        if gotcha_data == 'yes':
            calculator.data()
            result = None
            return render_template('index.html', result="result")
        
        invest = request.form.get('invest')
        if invest == 'yes':
            return render_template('index.html', result="2")

        
        keep = request.form.get('gotcha_data')
        if keep == 'yes':
            pass


    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
