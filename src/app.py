from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ 
    { 
        "label": "My first task", 
        "done": False 
        } 
    ]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_todo = request.json
    todos.append(request_todo)
    print("Incoming request with the following body", request_todo)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:ind>', methods=['DELETE'])
def delete_todo(ind):
    print("This is the position to delete:", ind)
    popped = todos.pop(ind)
    print("popped", popped)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)