from flask import Flask, json, request, jsonify
from scraper import mention_graph, mention_tree, get_social_circle
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello"

@app.route('/api/v1.0/mentions', methods=['GET'])
def get_mentions():
    if request.args.get('name'):
        name = request.args.get('name')
    else:
        return "Error"
    
    #tree = mention_tree(name)
    #graph = mention_graph(name)
    tree = get_social_circle(name)
    return json.dumps(tree)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    app.run(debug=True)