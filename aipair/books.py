import sqlite3

DB_PATH = 'books.db'

def create_book(title, author, year):
    """Insert a new book into the books table."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year)
    )
    conn.commit()
    book_id = cur.lastrowid
    conn.close()
    return book_id

def get_book(book_id):
    """Retrieve a book by its ID."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, year FROM books WHERE id = ?", (book_id,))
    book = cur.fetchone()
    conn.close()
    return book



def get_all_books():
    """Retrieve all books."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, year FROM books")
    books = cur.fetchall()
    conn.close()
    return books

def update_book(book_id, title=None, author=None, year=None):
    """Update a book's details."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    fields = []
    values = []
    if title is not None:
        fields.append("title = ?")
        values.append(title)
    if author is not None:
        fields.append("author = ?")
        values.append(author)
    if year is not None:
        fields.append("year = ?")
        values.append(year)
    values.append(book_id)
    sql = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"
    cur.execute(sql, values)
    conn.commit()
    conn.close()

def delete_book(book_id):
    """Delete a book by its ID."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

