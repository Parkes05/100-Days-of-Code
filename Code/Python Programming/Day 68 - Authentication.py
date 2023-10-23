from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

with app.app_context():
    db.create_all()
 
# CONNECT TO LOGIN MANAGER
login_manager = LoginManager(app)

# CREATE A USER LOADER CALLBACK
@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User, id)


@app.route('/')
def home():
    if login_user(current_user):
        logged_in=True
    else:
        logged_in = False
    return render_template("index.html", logged_in=logged_in)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if not db.session.execute(db.select(User).where(User.email == email)).scalar():
            new_user = User(
                name = name,
                email = email,
                password = generate_password_hash(request.form.get('password'), method='scrypt', salt_length=8),
                )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
        else:
            flash('Email already exists, login instead')
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        result = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if result:
            if check_password_hash(result.password, password):
                login_user(result)
                return redirect(url_for('secrets'))
            else:
                flash('Password incorrect, please try again')
                return render_template("login.html", email=email)
        else:
            flash('That email does not exist, please try again')
            return render_template("login.html")
    return render_template("login.html")


@app.route('/secrets', endpoint='secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf', as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
