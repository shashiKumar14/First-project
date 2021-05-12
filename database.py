from createTable import getDb


def insert(Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew):
    db = getDb()
    cursor = db.cursor()
    query= "INSERT INTO ProjectData(Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew) VALUES(?,?,?,?,?,?,?,?,?)"
    cursor.execute(query,[Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew])
    db.commit()
    return True

def update(id,Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew):
    db = getDb()
    cursor = db.cursor()
    query = "UPDATE ProjectData SET id=?,Ship_name=?,Cruise_line=?,Age=?,Tonnage=?, passengers=?,length=?,cabins=?,passenger_density=?,crew=? WHERE id = ?"
    cursor.execute(query, [id,Ship_name,Cruise_line,Age,Tonnage, passengers,length,cabins,passenger_density,crew])
    db.commit()
    return True


def delete(id):
    db = getDb()
    cursor = db.cursor()
    query = "DELETE FROM ProjectData WHERE id = ?"
    cursor.execute(query, [id])
    db.commit()
    return True


def getById(id):
    db = getDb()
    cursor = db.cursor()
    query= "SELECT * FROM ProjectData WHERE id = ?"
    cursor.execute(query, [id])
    return cursor.fetchone()

def getByName(Ship_name):
    db = getDb()
    cursor = db.cursor()
    query= "SELECT * FROM ProjectData WHERE Ship_name = ?"
    cursor.execute(query, [Ship_name])
    return cursor.fetchone()

def getData():
    db = getDb()
    cursor = db.cursor()
    query = "SELECT * FROM ProjectData"
    cursor.execute(query)
    return cursor.fetchall()
