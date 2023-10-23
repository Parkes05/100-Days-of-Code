from flask import Flask, render_template
import requests


response = requests.get(url='https://api.npoint.io/3c821def64f64845bdf0')
response.raise_for_status()
all_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Day 57 - Index.html", post=all_posts)

@app.route('/blog/<int:num>')
def my_blog(num):
    return render_template("Day 57 - Blog.html", number=num, post=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
