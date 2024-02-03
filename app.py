from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3

app = Flask(__name__)
# states = []

@app.route('/')
def index_page():  # put route applications's code here
    dorms = ["Stever", "Mudge", "Morewood Garden", "Morewood E-tower", "Mudge", "West Wing", "Resnik", "Donner", "The Hill"]
    buildings = ["Gates-Hillman", "Newell-Simon", "Wean", "Scott", "Hamerschlag", "Scaife", "ANSYS", "Porter", "Baker",
                "Hunt Library", "College of Fine Arts", "Posner", "Hall of the Arts", "Margaret Morrison", 
                "Cohon University Center", "Purnell Center for the Arts", "Tepper", "Mellon Institute", "Doherty"]
    return render_template('index.html', buildings=buildings, dorms = dorms)

@app.route('/route', methods=['POST'])
def route_page():  # put home applications's code here
    states = []
    states.append(request.form["dorms"])
    states.append(request.form["class1"])
    states.append(request.form["class2"])
    states.append(request.form["class3"])
    states.append(request.form["class4"])
    print(states)
    
    return render_template('route.html')

@app.route('/enterClasses')
def enterClasses_page():  # put home applications's code here
    return render_template('index.html')
    # states.append(request.form['dorm'])
    # states.append(request.form['state1'])
    # states.append(request.form['state2'])
    # states.append(request.form['state3'])
    # states.append(request.form['state4'])
