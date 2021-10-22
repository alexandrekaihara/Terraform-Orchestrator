import json
from flask import jsonify
import requests

def index():
    try:
        api = 'https://pokeapi.co/api/v2/pokemon'
        res = requests.get(api).json()
        return jsonify(res['results'])
    except:
        print("Houve algum erro.")
        return {
            'statusCode': 400,
            'body': json.dumps('Houve algum erro!')
        }


def show(name):
    try:
        api = 'https://pokeapi.co/api/v2/pokemon/{name}'.format(name=name)
        res = requests.get(api).json()
        return jsonify(res)
    except:
        print("Houve algum erro.")
        return {
            'statusCode': 400,
            'body': json.dumps('Houve algum erro!')
        }

def ability(id):
    try:
        api = 'https://pokeapi.co/api/v2/ability/{id}'.format(id=id)
        res = requests.get(api).json()
        return jsonify(res)
    except:
        print("Houve algum erro.")
        return {
            'statusCode': 400,
            'body': json.dumps('Houve algum erro!')
        }