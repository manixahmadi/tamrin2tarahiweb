from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongo = PyMongo(app)

# گرفتن همه کارها
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = mongo.db.tasks.find()
    result = []
    for task in tasks:
        result.append({
            'id': str(task['_id']),
            'title': task['title'],
            'description': task['description']
        })
    return jsonify(result)

# ایجاد کار جدید
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = {
        'title': data['title'],
        'description': data['description']
    }
    result = mongo.db.tasks.insert_one(task)
    return jsonify({'id': str(result.inserted_id)}), 201

# گرفتن کار خاص با id
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = mongo.db.tasks.find_one({'_id': ObjectId(id)})
    if task:
        return jsonify({
            'id': str(task['_id']),
            'title': task['title'],
            'description': task['description']
        })
    else:
        return jsonify({'error': 'Task not found'}), 404

# بروزرسانی کار با id
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.json
    updated = mongo.db.tasks.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'title': data['title'],
            'description': data['description']
        }}
    )
    if updated.matched_count:
        return jsonify({'message': 'Task updated'})
    else:
        return jsonify({'error': 'Task not found'}), 404

# حذف کار با id
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    deleted = mongo.db.tasks.delete_one({'_id': ObjectId(id)})
    if deleted.deleted_count:
        return jsonify({'message': 'Task deleted'})
    else:
        return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
