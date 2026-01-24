from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory tasks
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        status = request.form.get('status')
        priority = request.form.get('priority')
        if title and status and priority:
            new_id = max([task['id'] for task in TASKS], default=0) + 1
            TASKS.append({'id': new_id, 'title': title, 'status': status, 'priority': priority})
            return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/task/<int:id>')
def task_detail(id):
    task = next((task for task in TASKS if task['id'] == id), None)
    if not task:
        return "Task not found", 404
    return render_template('task.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    global TASKS
    TASKS = [task for task in TASKS if task['id'] != id]
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
