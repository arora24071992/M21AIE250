from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'some_secret_key'  # for flash messages

def init_db():
    with app.app_context():
        db = sqlite3.connect('books.db')
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                review TEXT
            );
        ''')
        db.commit()

@app.route('/')
def index():
    db = sqlite3.connect('books.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    author = request.form.get('author')
    review = request.form.get('review')
    if title and author:
        db = sqlite3.connect('books.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO books(title, author, review) VALUES(?, ?, ?)', (title, author, review))
        db.commit()
        flash('Book added successfully!')
    else:
        flash('Title and Author are required!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')

