from flask import Flask, render_template, url_for, request
from logging import DEBUG
import main


app = Flask(__name__)
app.logger.setLevel('DEBUG')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        url = request.form['url']
        return render_template('calculate.html', value=str(main.calculate(url)))
    else:
        url = request.args.get('url')
        return render_template('calculate.html', value=str(main.calculate(url)))


if __name__ == '__main__':
    app.run(debug=True)
