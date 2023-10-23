from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from Forms_69 import CreatePostForm, RegisterForm, LoginForm, CommentForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# CONFIGURE TABLES
class BlogPost(db.Model): #Child #Parent
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship('Comment', back_populates='post')
    
class User(UserMixin, db.Model): #Parent
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    posts = relationship('BlogPost', back_populates='author')
    comments = relationship('Comment', back_populates='author')

class Comment(db.Model): #Child #Child
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    author = relationship('User', back_populates='comments')
    post = relationship('BlogPost', back_populates='comments')
    text = db.Column(db.Text, nullable=False)

# CONFIGURE GRAVATAR
gravatar = Gravatar(
    app,
    size=100,
    rating='g',
    default='retro',
    force_default=False,
    force_lower=False,
    use_ssl=False,
    base_url=None
    )

with app.app_context():
    db.create_all()

# DECORATOR FUNCTION
def admin_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return function(*args, **kwargs)
    return wrapper

# CONFIGURE FLASK LOGIN
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(id):
    return db.get_or_404(User, id)


# WEBSITE ROUTES
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash('You\'ve already signed up with that email, login instead')
            return redirect(url_for('login'))
        else:
            name = register_form.name.data
            hashed_password = generate_password_hash(register_form.password.data, method='scrypt', salt_length=16)
            new_user = User(
                name=name,
                email=email,
                password=hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash('That email does not exist, please try again')
            return render_template("login.html", form=login_form)
        elif check_password_hash(user.password, login_form.password.data):
            login_user(user)
            print(current_user.name)
            return redirect(url_for('get_all_posts'))
        else:
            flash('Password incorrect, please try again')
            return render_template("login.html", form=login_form)
    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>", methods = ['GET', 'POST'])
def show_post(post_id):
    if current_user.is_authenticated:
        comment_form = CommentForm()
        if comment_form.validate_on_submit():
            new_comment = Comment(
                text = comment_form.comment.data,
                author_id = current_user.id,
                post_id = post_id,
                )
            db.session.add(new_comment)
            db.session.commit()
    else:
        comment_form = False
        flash('Login to post a comment')
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post, form=comment_form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        post.author_id = current_user.id
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
