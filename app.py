from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main-1')
def main_1():
    return render_template('main1.html')

@app.route('/main-2')
def main_2():
    return render_template('main2.html')

@app.route('/main-3')
def main_3():
    return render_template('main3.html')

@app.route('/main-4')
def main_4():
    return render_template('main4.html')

@app.route('/main-5')
def main_5():
    return render_template('main5.html')


if __name__ == '__main__':
    app.run(debug=True)
