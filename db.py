import os
import sqlite3
from werkzeug.security import generate_password_hash

database_path = "./data/topaz.sqlite"


def init_db():
    """
    Create database and tables if it isn't present

    """
    if os.path.exists(database_path):
        return
    # Create database and tables
    db = get_db()
    c = db.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    c.execute("CREATE TABLE public_repos (id INTEGER PRIMARY KEY, title TEXT, description TEXT, readme TEXT, "
              "latest_commit TEXT, url TEXT, image_url TEXT, timestamp TEXT)")
    c.execute("CREATE TABLE blogs (id INTEGER PRIMARY KEY, title TEXT, description TEXT, "
              "url TEXT, image_url TEXT, timestamp TEXT)")
    c.execute("CREATE TABLE publications (id INTEGER PRIMARY KEY, title TEXT, description TEXT, "
              "url TEXT, image_url TEXT, timestamp TEXT)")

    # Create admin
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (os.getenv("USERNAME"),
                                                                       generate_password_hash(os.getenv("PASSWORD"))))
    db.commit()
    db.close()


def get_db():
    """
    Returns a database connection and sets output for be like dicts

    Returns (db object): sqlite3 db object

    """
    db = sqlite3.connect(database_path)
    db.row_factory = sqlite3.Row
    return db
