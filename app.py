from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
from searchFunction import *

app = Flask(__name__)
states = []
def search(states):
    mealIndex=states.index("MEAL")
    print(states)
    print(states[mealIndex])
    states[mealIndex]=closestMeal(find(states[mealIndex-1])[0][0], find(states[mealIndex-1])[0][1])


    path1=doSearch(states[0], states[1])
    path2=doSearch(states[1], states[2])
    path3=doSearch(states[2], states[3])
    path4=doSearch(states[3], states[4])
    path5=doSearch(states[4], states[5])
    path6=doSearch(states[5], states[0])




    pixelGrid1= iio.imread("./Search Code/cmu_map_small.png", pilmode="RGB")
    for locn in path1:
        row=locn[0]
        col=locn[1]
        pixelGrid1[row][col]=[63,255,63]
    img1 = Image.fromarray(pixelGrid1.astype(np.uint8) * 255, mode='RGB')
    img1 = img1.save("/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route1.png")

    pixelGrid2= iio.imread("./Search Code/cmu_map_small.png", pilmode="RGB")
    for locn in path2:
        row=locn[0]
        col=locn[1]
        pixelGrid2[row][col]=[63,255,63]
    img2 = Image.fromarray(pixelGrid2.astype(np.uint8) * 255, mode='RGB')
    img2 = img2.save("/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route2.png")

    pixelGrid3= iio.imread("./Search Code/cmu_map_small.png", pilmode="RGB")
    for locn in path3:
        row=locn[0]
        col=locn[1]
        pixelGrid3[row][col]=[63,255,63]
    img3 = Image.fromarray(pixelGrid3.astype(np.uint8) * 255, mode='RGB')
    img3 = img3.save("/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route3.png")

    pixelGrid4= iio.imread("./Search Code/cmu_map_small.png", pilmode="RGB")
    for locn in path4:
        row=locn[0]
        col=locn[1]
        pixelGrid4[row][col]=[63,255,63]
    img4 = Image.fromarray(pixelGrid4.astype(np.uint8) * 255, mode='RGB')
    img4 = img4.save("/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route4.png")

    pixelGrid5= iio.imread("./Search Code/cmu_map_small.png", pilmode="RGB")
    for locn in path5:
        row=locn[0]
        col=locn[1]
        pixelGrid5[row][col]=[63,255,63]
    img5 = Image.fromarray(pixelGrid5.astype(np.uint8) * 255, mode='RGB')
    img5 = img5.save("/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route5.png")

    pixelGrid6= iio.imread("./Search Code/cmu_map_small.png", pilmode="RGB")
    for locn in path6:
        row=locn[0]
        col=locn[1]
        pixelGrid6[row][col]=[63,255,63]
    img6 = Image.fromarray(pixelGrid6.astype(np.uint8) * 255, mode='RGB')
    img6 = img6.save("/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route6.png")
    return (["/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route1.png", 
             "/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route2.png", 
             "/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route3.png", 
             "/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route4.png",
              "/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route5.png", 
              "/Users/pranavikondapalli/Desktop/CMU_ROUTES/static/route6.png"], closestMeal(find(states[mealIndex-1])[0][0], find(states[mealIndex-1])[0][1]))

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
    # states = []
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
    dorms=request.form["dorms"]
    class1= request.form["class1"]
    class2=request.form["class2"]
    class3 = request.form["class3"]
    class4 = request.form["class4"]
    places = [dorms, class1, class2, class3, class4]
    
    states = []
    states.append(dormsShort.get(request.form["dorms"]))
    states.append(buildingsShort.get(request.form["class1"]))
    states.append(buildingsShort.get(request.form["class2"]))
    states.append(buildingsShort.get(request.form["class3"]))
    states.append(buildingsShort.get(request.form["class4"]))
    states.insert(whenMeal, "MEAL")
    solution=search(states)
    images = solution[0];
    places.insert(whenMeal, solution[1])
    places.append(dorms)


    return render_template('route.html', images=images, places=places)

@app.route('/enterClasses')
def enterClasses_page():  # put home applications's code here
    return render_template('index.html')
    # states.append(request.form['dorm'])
    # states.append(request.form['state1'])
    # states.append(request.form['state2'])
    # states.append(request.form['state3'])
    # states.append(request.form['state4'])


    