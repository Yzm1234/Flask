#!/usr/bin/env python3
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
import requests, json

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def hello():
    return 'This the the home page <h1>HELLO, welcome to the homepage!</h1>'


@app.route('/pokemon', methods=['GET', 'POST', 'PUT'])
def poke():
    if request.method == 'GET':
        data = []
        name_url = "https://pokeapi.co/api/v2/pokemon?limit=50"
        while True:
            resp = requests.get(name_url)
            json = resp.json()
            data.extend(json.get('results', []))
            name_url = json.get('next')
            if not name_url: break
        return jsonify({'data': json})

    elif request.method == 'POST':
        m = request.form
        return jsonify({'echo': m})


    elif request.method == 'PUT':
        m = request.form
        return jsonify({'echo': m})


if __name__ == '__main__':
   app.run(debug = True)