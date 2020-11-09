import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p><hr>
<p>Type <i><b>/books</b></i> in the url to view all the books in json format</p><br>
<p>For finding a particular book mention it's id in the following url. For Example - <i><b>/books/1</b></i></p>'''


# A route to return all of the available entries in our catalog.
@app.route('/books', methods=['GET'])
def api_all():
    return jsonify(books)
    
#when any wrong route will be entered. 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

#returns the book in json format with given id. 
@app.route('/books/<int:id>', methods=['GET'])
def api_id(id:int):
    if 'id':
        id = int(id)
    else:
        return "Error: No id field provided. Please specify an id."
results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)
    
    
app.run()
