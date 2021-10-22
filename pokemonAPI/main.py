from flask import Flask, request

from methods import index, show, ability


app = Flask(__name__)

@app.route('/pokemon', methods=['GET'])
def pokemon_index():
    return index()

@app.route('/pokemon/<name>', methods=['GET'])
def pokemon_show(name):
    return show(name)

@app.route('/ability/<id>', methods=['GET'])
def ability_info(id):
    return ability(id)

app.run(host="0.0.0.0", port = 2000, debug = False)