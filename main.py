from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for the todo list (replace this with a database later)
todos = []


@app.route('/')
def index():
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            todos.append(task)
    return redirect(url_for('index'))


@app.route('/delete/<task>', methods=['POST'])
def delete_todo(task):
    todos.remove(task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
