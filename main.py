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
            return render_template('index.html', result=result)

       # Get "Gotcha!" data

        # Check if "Gotcha!" button was clicked and store data in CSV
        elif 'gotcha_data' in request.form:
            gotcha_data = request.form.get('gotcha_data')  # Get "Gotcha!" data
            if gotcha_data == 'yes':
                calculator.data()
                result = None
                return render_template('index.html', result=result)
    
        if any(key.startswith('invest_') for key in request.form.keys()):
            alternative_result = "To be continued"
            # Do your action for the invest button here
            return render_template('index.html', alternative_result=alternative_result)
        
    return render_template('index.html', result=result)  # Default return statement

if __name__ == '__main__':
    app.run(debug=True)
