from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    url = StringField(label='Location URL', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opening Time', validators=[DataRequired()])
    close_time = StringField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=['☕'*num for num in [1,2,3,4,5]], validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Rating', choices=['💪'*num for num in [1,2,3,4,5]], validators=[DataRequired()])
    outlet_rating = SelectField(label='Power Outlet Rating', choices=['⚡'*num for num in [1,2,3,4,5]], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    form.coffee_rating.choices.insert(0, '✘')
    form.wifi_rating.choices.insert(0, '✘')
    form.outlet_rating.choices.insert(0, '✘')

    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csvfile:
            data = csv.writer(csvfile)
            data.writerow([value for (key, value) in form.data.items() if key != 'csrf_token'])
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
