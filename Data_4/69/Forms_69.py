from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, URLField, EmailField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = URLField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# WTForm for registering users
class RegisterForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Register')


# LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


# CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField(label='comment', validators=[DataRequired()])
    submit = SubmitField(label='Submit Comment')
