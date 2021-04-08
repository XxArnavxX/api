from flask import Flask, request, jsonify
app = Flask(__name__)
tasks = [{
    'id': 1,
    'title' : u'buy groceries',
    'description': u'milk, fruits, cheese, pizza, vegetables, chocolate, chips, and cold drinks',
    'done': False,
},{
    'id': 2,
    'title' : u'learn python',
    'description': u'find python tutorial online',
    'done': False,
}]
@app.route("/")
def helloWorld():
    return"hello world"

@app.route("/add-data", methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({"status": "error", "message": "please provide the data"}, 400)
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get("description", ""),
        'done': False,
    }
    tasks.append(task)
    return jsonify({"status": 'success', "message": "task added successfully"})
@app.route("/get-data")
def getTask():
    return jsonify({"data": tasks})
if(__name__=="__main__"):
    app.run(debug=True)