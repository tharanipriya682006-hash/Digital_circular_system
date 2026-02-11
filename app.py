from flask import Flask,render_template,request,redirect,session
from flask_mysqldb import MySQL

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tharanipriya",
    database="hackathon"
)


