from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_list.db'
db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(5), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()


class ReviewForm(FlaskForm):
    rating = StringField(label='Your rating out of 10 e.g 6.5', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

class MovieTitle(FlaskForm):
    title = StringField(label='MovieTitle', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')

@app.route("/")
def home():
    result = list(db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars())
    return render_template("index.html", movies=result)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    review_form = ReviewForm()
    if review_form.validate_on_submit():
        new_rating = float(review_form.rating.data)
        new_review = review_form.review.data
        update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        update.rating = new_rating
        update.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html', form=review_form)


@app.route('/delete/<id>')
def delete(id):
    delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_title = MovieTitle()
    if movie_title.validate_on_submit():
        headers = {
        "accept": "application/json",
        "Authorization": ""
        }
        response = requests.get(url='https://api.themoviedb.org/3/authentication', headers=headers)
        response.raise_for_status()

        print(response.text)

        title = movie_title.title.data
        return render_template('select.html', title=title)
    return render_template('add.html', form=movie_title)


if __name__ == '__main__':
    app.run(debug=True)
