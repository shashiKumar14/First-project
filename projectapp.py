from flask import Flask,jsonify,request
import database
from createTable import createTables

app = Flask(__name__)

@app.route('/ProjectData',methods=['POST'])
def insert():
    data = request.get_json()
    Ship_name = data["Ship_name"]
    Cruise_line = data["Cruise_line"]
    Age= data["Age"]
    Tonnage=data["Tonnage"]
    passengers=data["passengers"]
    length=data["length"]
    cabins=data["cabins"]
    passenger_density=data["passenger_density"]
    crew=data["crew"]
    output = database.insert(Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew)
    return jsonify(output)

@app.route('/ProjectData',methods=["PUT"])
def update():
    data = request.get_json()
    id = data["id"]
    Ship_name = data["Ship_name"]
    Cruise_line = data["Cruise_line"]
    Age= data["Age"]
    Tonnage=data["Tonnage"]
    passengers=data["passengers"]
    length=data["length"]
    cabins=data["cabins"]
    passenger_density=data["passenger_density"]
    crew==data["crew"]
    output = database.update(id,Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew)
    return jsonify(output)

@app.route('/ProjectData/<id>',methods=["DELETE"])
def delete(id):
    output = database.delete(id)
    return jsonify(output)

@app.route('/getData',methods=['GET'])
def getData():
    get = database.getData()
    return jsonify({'database' : get})

@app.route('/ProjectData/<id>')
def getById(id):
    dataById = database.getById(id)
    return jsonify(dataById)

@app.route('/ProjectData/<string:name>')
def getByName(Ship_name):
    dataByName = database.getByName(Ship_name)
    return jsonify(dataByName)

if __name__ == "__main__":
    createTables()
    app.run(debug=True)
