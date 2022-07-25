from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animal.db'
app.config['QLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Comment %r' % self.id


@app.route('/comment',  methods=['POST', 'GET'])
def create_comment():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        comment = Comment(title=title, text=text)

        try:
            db.session.add(comment)
            db.session.commit()
            return redirect('/all_comments')
        except:
            return 'Произошла ошибка'
    else:
        return render_template('comment.html')


@app.route('/all_comments')
def all_comments():
    comments = Comment.query.order_by(Comment.date.desc()).all()
    return render_template('all_comments.html', comments=comments)


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
