# 3. Write an Rest API
#     - Take the column name as input
#     - Respond with highest and lowest values in column
from flask import Flask,jsonify
import pandas as pd

df=pd.read_csv('cruise_ship_info.csv')#appending of csv file int df with the help of read_csv

app=Flask(__name__)

@app.route('/Age')#input as Age
def Age():
    min=df['Age'].min()
    max=df['Age'].max()
    return jsonify({'min':min,"max":max})# displaying  min and max of Age

@app.route('/Tonnage')#input as Tonnage
def Tonnage():
    min1=df['Tonnage'].min()
    max1=df['Tonnage'].max()
    return jsonify({'min':min1,"max":max1})#displaying min and max of Tonnage

@app.route('/passengers')#input as passengers
def passengers():
    min1=df['passengers'].min()
    max1=df['passengers'].max()
    return jsonify({'min':min1,"max":max1})#displaying min and max of passengers

@app.route('/length')#input as length
def length():
    min1=df['length'].min()
    max1=df['length'].max()
    return jsonify({'min':min1,"max":max1})#displaying min and max of length

@app.route('/cabins	')#input as cabins
def cabins():
    min1=df['cabins'].min()
    max1=df['cabins'].max()
    return jsonify({'min':min1,"max":max1})#displaying min and max of cabins

@app.route('/passenger_density')#input as passenger_density
def passenger_density():
    min1=df['passenger_density'].min()
    max1=df['passenger_density'].max()
    return jsonify({'min':min1,"max":max1})#displaying min and max of passenger_density

@app.route('/crew')#input as crew
def crew():
    min1=df['crew'].min()
    max1=df['crew'].max()
    return jsonify({'min':min1,"max":max1})#displaying min and max of crew


if __name__ == '__main__':
    app.run(debug=True)
 

# from flask import Flask,jsonify
# import pandas as pd
#
# df=pd.read_csv('cruise_ship_info.csv')#appending of csv file int df with the help of read_csv
#
# app=Flask(__name__)
#
# @app.route('/<string:name>')#input as Age
# def get(name):
#     min=df[name].min()
#     max=df[name].max()
#     return jsonify({'min':min,"max":max})#
