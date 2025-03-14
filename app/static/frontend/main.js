document.addEventListener("DOMContentLoaded", function() {
    const taskForm = document.getElementById("task-form");
    const taskList = document.getElementById("task-list");


    function fetchTasks() {
        fetch("http://127.0.0.1:5000/tasks")
            .then(response => response.json())
            .then(data => {
                taskList.innerHTML = "";
                data.forEach(task => {
                    const li = document.createElement("li");
                    li.innerHTML = `${task.title} - <strong>${task.status}</strong>
                        <button onclick="deleteTask(${task.id})">Delete</button>
                        <button onclick="toggleStatus(${task.id})">Toggle Status</button>`;
    
                    li.onclick = function() {
                        alert(`Title: ${task.title}\nDescription: ${task.description}\nStatus: ${task.status}`);
                    };
    
                    taskList.appendChild(li);
                });
            });
    }
    
    // Toggle status function
    window.toggleStatus = function(id) {
        fetch(`http://127.0.0.1:5000/tasks/${id}/toggle`, { method: "PATCH" })
            .then(() => fetchTasks());
    };


    // Add task
    taskForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const title = document.getElementById("task-title").value;
        const description = document.getElementById("task-desc").value;

        fetch("http://127.0.0.1:5000/tasks", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, description })
        })
        .then(() => {
            taskForm.reset();
            fetchTasks();
        });
    });

    // Delete task with confirmation
    window.deleteTask = function(id) {
        if (confirm("Are you sure you want to delete this task?")) {
        fetch(`http://127.0.0.1:5000/tasks/${id}`, { method: "DELETE" })
            .then(() => fetchTasks());
        }};

    fetchTasks();
});