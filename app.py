import sqlite3
import sys
from flask import Flask, render_template, url_for, request, redirect
from database_handler import database_start, database_read

app = Flask(__name__)

#Home
@app.route('/')
def home():
    database_start()
    return render_template('home.html', page_name="About Me", staff=database_read())

@app.route('/:)')
def smile():
    return "<p>:)</P"

#Error handling
@app.errorhandler(404)
def error_page_not_found(error):
    return redirect('/')

@app.errorhandler(500)
def error_page_server_error(error):
    return redirect('/:)')

#Launch Website
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)