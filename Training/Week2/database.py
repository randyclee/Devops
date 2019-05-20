#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
from flask_api import FlaskAPI
import sys
import math
from instance.config import app_config
from PIL import Image
from flask import request, jsonify, abort

def create_app(config_name):
    from week2.models import Location
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/locations/', methods=['PRINTALL', 'FILTER','DISTANCE'])
    def locations():
        if request.method == "PRINTALL":
            con = lite.connect('user.db')
            with con:
                #print all
                cur = con.cursor()
                cur.execute("SELECT * FROM Location")

                rows = cur.fetchall()

                for row in rows:
                    print row
                response.status_code = 201
              return response

        if request.method == "FILTER":
            #filtering from category
            results = []
            con = lite.connect('user.db')
            with con:
                filter = raw_input("enter search: ");
                cur.execute("SELECT * FROM Locations WHERE Category = '"+filter+ "'")
                rows = cur.fetchall()
                for row in rows:
                    print row
                    results.append(obj)
                response = jsonify(results)
                response.status_code = 200
                return response

        if request.method == "Distance":
        #distance
            con = lite.connect('user.db')
            with con:
                filter = raw_input("enter location 1 name: ");
                cur.execute("SELECT long FROM Locations WHERE name = '"+filter+ "'")
                rows = cur.fetchall()
                for row in rows:
                    input1x = row[0]
                cur.execute("SELECT lat FROM Locations WHERE name = '"+filter+ "'")
                rows = cur.fetchall()
                for row in rows:
                    input1y= row[0]
                point1 = (int(input1x)*int(input1x)+int(input1y)*int(input1y))
                point1 = math.sqrt(point1)
                print(point1)
                filter = raw_input("enter location 2 name: ");
                cur.execute("SELECT long FROM Locations WHERE name = '"+filter+ "'")
                rows = cur.fetchall()
                for row in rows:
                    input2x= row[0]
                    print(point2x)
                cur.execute("SELECT lat FROM Locations WHERE name = '"+filter+ "'")
                rows = cur.fetchall()
                for row in rows:
                    input2y= row[0]
                    print(point2y)

                point2 = (int(input2x)*int(input2x)+int(input2y)*int(input2y))
                point2 = math.sqrt(point2)
                answer = math.abs(point2-point1)
                print(answer)
                response = answer

                img = Image.new( 'RGB', (250,250), "black") # create a new black image
                pixels = img.load() # create the pixel map

                for i in range(img.size[0]):    # for every col:
                    for j in range(img.size[1]):    # For every row
                        pixels[i,j] = (255, 255, 255) # set the colour accordingly
                pixels[point1x,point1y] = (100, 100, 100) # set the colour accordingly
                pixels[point2x,point2y] = (100, 100, 100) # set the colour accordingly

                img.show()

                response.status_code = 200
                return response
        return app
