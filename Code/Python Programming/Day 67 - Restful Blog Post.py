from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# CONNECT TO BOOTSTRAP
Bootstrap5(app)

# CONNECT TO CKEDITOR
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# CREATE FORM
class BlogForm(FlaskForm):
    title = StringField(label='Blog Post Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    img_url = StringField(label='Background Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField(label='Blog Content', validators=[DataRequired()])
    submit = SubmitField(label='Submit Post')


with app.app_context():
    db.create_all()

@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/blog/<post_id>')
def show_post(post_id):
    result = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=result)


@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        x = datetime.now()
        db.session.add(
            BlogPost(
                title=blog_form.title.data,
                subtitle=blog_form.subtitle.data,
                date=f'{x.strftime("%B")} {x.day}, {x.year}',
                body=blog_form.body.data,
                author=blog_form.author.data,
                img_url=blog_form.img_url.data,
            )
        )
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=blog_form)


@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    x = db.get_or_404(BlogPost, post_id)
    form = BlogForm(
        title=x.title,
        subtitle=x.subtitle,
        body=x.body,
        author=x.author,
        img_url=x.img_url,
    )
    if form.validate_on_submit():
        x.title = form.title.data
        x.subtitle = form.subtitle.data
        x.body = form.body.data
        x.author = form.author.data
        x.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=x.id))
    return render_template('make-post.html', id=post_id, form=form)


@app.route('/delete/<post_id>')
def delete(post_id):
    delete_entry = db.get_or_404(BlogPost, post_id)
    db.session.delete(delete_entry)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
