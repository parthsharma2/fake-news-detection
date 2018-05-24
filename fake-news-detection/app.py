from flask import Flask, render_template, url_for, request
from logging import DEBUG


app = Flask(__name__)
app.logger.setLevel('DEBUG')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
