from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# -----------------------------
# OPEN LOGIN PAGE
# -----------------------------
@app.route('/')
def home():
    return render_template('login.html')


# -----------------------------
# HANDLE LOGIN FORM
# -----------------------------
@app.route('/login', methods=['POST'])
def login():

    role = request.form['role']
    username = request.form['username']
    password = request.form['password']

    # TEMPORARY LOGIN CHECK (you can connect MySQL later)
    if username == "admin" and password == "1234" and role == "admin":
        return "Admin Login Successful"

    else:
        return "Invalid Login"


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
