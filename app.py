from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3

app = Flask(__name__)
# states = []

@app.route('/')
def index_page():  # put home applications's code here
    dorms = ["Stever", "Mudge", "Morewood Garden", "Morewood E-tower", "Mudge", "West Wing", "Resnik", "Donner", "The Hill"]
    buildings = ["Gates-Hillman", "Newell-Simon", "Wean", "Scott", "Hamerschlag", "Scaife", "ANSYS", "Porter", "Baker",
                "Hunt Library", "College of Fine Arts", "Posner", "Hall of the Arts", "Margaret Morrison", 
                "Cohon University Center", "Purnell Center for the Arts", "Tepper", "Mellon Institute", "Doherty"]
    mealTimes = ["Before Class 1", "Between Class 1 and 2", "Between Class 2 and 3", "Between Class 3 and 4","After Class 4"]
    return render_template('index.html', buildings=buildings, dorms = dorms, mealTimes = mealTimes)

@app.route('/route', methods=['POST'])
def route_page():  # put route applications's code here
    states = []
    dormsShort = {"Stever": "STE",
            "Morewood E-tower": "MOE",
            "Morewood Garden": "MOR",
            "Mudge": "MUD",
            "West Wing": "WWG",
            "Resnik": "RES",
            "Donner": "DON",
            "The Hill": "HILL",}
    buildingsShort = { "Gates-Hillman":"GHC",
                        "Newell-Simon": "NSH",
                        "Wean": "WEH",
                        "Scott": "SC",
                        "Hamerschlag": "HH",
                        "Scaife": "SH",
                        "ANSYS": "ANSYS",
                        "Porter": "PH",
                        "Baker": "BH",
                        "Hunt Library": "HUNT",
                        "College of Fine Arts": "CFA",
                        "Posner": "POS",
                        "Hall of the Arts": "HOA",
                        "Margaret Morrison": "MM",
                        "Cohon University Center": "CUC",
                        "Purnell Center for the Arts": "PCA",
                        "Tepper": "TEP",
                        "Mellon Institute": "MI",
                        "Doherty": "DH"}
    mealTimeDict = {"Before Class 1": 1,
                    "Between Class 1 and 2":2,
                    "Between Class 2 and 3":3,
                    "Between Class 3 and 4":4,
                    "After Class 4":5,
                    }
    whenMeal = mealTimeDict.get(request.form["mealTime"])
    states.append(dormsShort.get(request.form["dorms"]))
    states.append(buildingsShort.get(request.form["class1"]))
    states.append(buildingsShort.get(request.form["class2"]))
    states.append(buildingsShort.get(request.form["class3"]))
    states.append(buildingsShort.get(request.form["class4"]))
    states.insert(whenMeal, "MEAL")
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
