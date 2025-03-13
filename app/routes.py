from flask import request, jsonify
from app import app, db
from app.models import Task

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'), status=data.get('status', 'pending'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully!'}), 201

# Get All Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "description": task.description ,"status": task.status} for task in tasks]
    return jsonify(task_list), 200

# Update Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)  # Find the task or return 404
    data = request.get_json()  # Get JSON data from request

    # Update fields if they exist in the request
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:  # Fix: Changed from 'completed' to 'status'
        task.status = data['status']

    db.session.commit()  # Save changes to database
    #return jsonify({'message': 'Task updated'})
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status  # Fix: Changed from 'completed' to 'status'
    }), 200

# Delete Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully!'}), 200
