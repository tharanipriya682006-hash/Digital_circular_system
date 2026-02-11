import mysql.connector
from flask import g

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="youruser",
            password="yourpass",
            database="yourdb"
        )
    return g.db

@app.teardown_appcontext

def close_db(error):
    db = g.pop('db', None)
    if db:
        db.close()


