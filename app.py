from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3

app = Flask(__name__)
# states = []

@app.route('/')
def route_page():  # put route applications's code here
    states = ["Stever", "Gates-Hillman", "Posner", "Scott", "UC"]
    return render_template('route.html', states=states)

@app.route('/route')
def index_page():  # put home applications's code here
    return render_template('index.html')

@app.route('/enterClasses')
def enterClasses_page():  # put home applications's code here
    return render_template('index.html')
    # states.append(request.form['dorm'])
    # states.append(request.form['state1'])
    # states.append(request.form['state2'])
    # states.append(request.form['state3'])
    # states.append(request.form['state4'])
