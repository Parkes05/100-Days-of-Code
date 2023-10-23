from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


# db = sqlite3.connect('Book_collection.db')
# cursor = db.cursor()

# cursor.execute("CREATE TABLE Books (id INT PRIMARY KEY, Title TEXT NOT NULL UNIQUE, Author TEXT NOT NULL, Rating REAL NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Moxy', 'Test', '9.5')")
# db.commit()


# # Create Records
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

# # Read All Records
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()

# # Read Single Element
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# # Update A Record
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit() 

# # Update A record By Primary Key 
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)  
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit() 

# # Delete A Record
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Book_collection.db"

db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
        result = list(db.session.execute(db.select(Book).order_by(Book.id)).scalars())
        return render_template('index.html', books=result)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        name = data['book-name']
        author = data['author']
        rating = data['rating']
        with app.app_context():
            entry = Book(title=name, author=author, rating=rating)
            db.session.add(entry)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        data = request.form
        new_rating = data['new-rating']
        update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    result = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    return render_template('edit.html', name=result.title, rating=result.rating, id=result.id)


@app.route('/delete/<id>')
def delete(id):
    delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

