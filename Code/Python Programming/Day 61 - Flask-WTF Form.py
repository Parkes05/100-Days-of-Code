from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')

app = Flask(__name__)
app.secret_key = 'testing'

bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    my_form = MyForm()
    if my_form.validate_on_submit():
        if my_form.email.data == 'admin@email.com' and my_form.password.data == '12345678':
            return render_template('success.html', form=my_form)
        else:
            return render_template('denied.html', form=my_form)
    return render_template('login.html', form=my_form)



if __name__ == '__main__':
    app.run(debug=True)