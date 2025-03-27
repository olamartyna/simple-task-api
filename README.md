# simple-task-api
# Simple Task Management API & Frontend

## Project description
This is a **simple task management app** built with Flask (Python) for the backend and vanilla JavaScript (HTML/CSS) for the frontend. The purpose of this project is to showcase my ability to build a complete **RESTful API** and integrate it with a frontend.
This project demonstrates **CRUD (Create, Read, Update, Delete)** operations and **SQLite database**.
<br /><br />

## Features
- **Create** a new task, with title and descripton
- **View** all tasks
- **Update** a task's status (pending/complete)
- **Delete** a task (with confirmation prompt)
- **Simple UI** with a task list and buttons for actions
- **Frontend & Backend Integration**
<br /><br />

## Tech Stack
- **Backend**: Flask, Flask-SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Tools**: Postman (for API testing), Git/GitHub
<br /><br />

## Installation and setup
1. Clone the repository
```
git clone https://github.com/yourusername/simple-task-api.git
cd simple-task-api
```
2. Create and activate a virtual environment
```
python -m venv simple-task-venv
source simple-task-venv/Scripts/activate   # on Windows
source simple-task-venv/bin/activate       # on macOS/Linux
```
3. install dependencies
```
pip install -r requirements.txt
```
4. Set up the database
```
python create_db.py
```
5. Run the application
```
flask run
```
Open ```http://127.0.0.1:5000/``` in your browser
<br /><br />

## Usage
**API endpoints**
|Method|Endpoint|Description|
|------|--------|-----------|
|GET|`/tasks`|Get all tasks|
|POST|`/tasks`|Create a task|
|GET|`/tasks/<id>`|Get a task|
|PUT|`/tasks/<id>`|Update a task|
|DELETE|`/tasks/<id>`|Delete a task|

**Frontend**
- Go to ```http://127.0.0.1:5000/```
- Add a task using the form
- CLick a task to view details
- Toggle status (pending/complete)
- Delete a task (with a confirmation modal)
- View all tasks
<br /><br />

## Future improvements
- Deploy online (using Heroku)
- Add authentication (user login/signup)
- Improve UI design with a framework (Bootstrap)
- Add filters (e.g. showing only completed tasks or tasks categories)
