from flask import Flask, app, json, request, jsonify
import networkx as nx
from networkx.readwrite import json_graph
from scraper import mention_graph
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Hello"


@app.route('/api/v1.0/mentions', methods=['GET'])
def get_mentions():
    if request.args.get('name'):
        name = request.args.get('name')
    else:
        return "Error"

    graph = mention_graph(name)
    return json_graph.node_link_data(graph)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run(debug=True)
