from flask import request, jsonify
from app import app, db
from app.models import Task

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data['title'], 
        description=data.get('description'), 
        status=data.get('status', 'pending')
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": f"Task '{new_task.title}' created successfully!"}), 201


# Get All Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        }
        for task in tasks
    ]

    return jsonify(task_list), 200


# Get Single Task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }), 200


# Update Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully!",
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        }
    }), 200


# Delete Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": f"Task '{task.title}' (ID: {task.id}) deleted successfully!"}), 200
