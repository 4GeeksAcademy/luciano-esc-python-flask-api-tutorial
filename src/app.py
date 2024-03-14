from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    
    return jsonify(todos)

@app.route('/todos/<int:ind>', methods=['DELETE'])
def delete_todo(ind):
    td_mutate=todos.pop(ind)
    return jsonify(f"data deleted = {(td_mutate)}")

@app.route('/todos/<int:id>', methods=['PUT'])
def put_todo(id):
    request_body = request.json
    for elm in todos:
        if elm['id'] == id:
            elm['done']==request_body['done']
    return jsonify(f"You changed {todos['done']}")
    





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)