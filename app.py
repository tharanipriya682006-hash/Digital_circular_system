import importlib
from flask import g, current_app

# Try to import mysql.connector (mysql-connector-python). If it's not
# available, provide a clear runtime error explaining how to install it.
mysql = importlib.import_module('mysql.connector') if importlib.util.find_spec('mysql.connector') else None

def get_db():
    if mysql is None:
        raise RuntimeError("Missing dependency: mysql-connector-python. Install with: python -m pip install mysql-connector-python")
    if 'db' not in g:
        g.db = mysql.connect(
            host=current_app.config.get('DB_HOST', 'localhost'),
            user=current_app.config.get('DB_USER', 'youruser'),
            password=current_app.config.get('DB_PASSWORD', 'yourpass'),
            database=current_app.config.get('DB_NAME', 'yourdb')
        )
    return g.db

def close_db(error=None):
    db = g.pop('db', None)
    if db:
        try:
            db.close()
        except Exception:
            pass

def init_app(app):
    """Register database teardown with the Flask app.

    Call `init_app(app)` from your application factory or main module after
    configuring `app.config['DB_HOST']`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.
    """
    app.teardown_appcontext(close_db)


