from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# LOGIN PAGE
@app.route("/")
def home():
    return render_template("login.html")


# LOGIN FORM SUBMIT
@app.route("/login", methods=["POST"])
def login():

    role = request.form["role"]
    username = request.form["username"]
    password = request.form["password"]

    # dummy check (you can connect database later)
    if username == "admin" and password == "1234":
        return "Login Successful 🎉"
    else:
        return "Invalid login ❌"


if __name__ == "__main__":
    app.run(debug=True)
