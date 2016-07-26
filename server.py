from flask import Flask, render_template, request, redirect
import pg

db = pg.DB('todo_db')

app = Flask('MyTodo')

@app.route('/')
def tasks():
    query = db.query('''
        select
            *
        from
            task
        order by
            task.name
    ''')
    return render_template(
        'list.html',
        title='Todo List',
        tasks=query.namedresult())

@app.route('/add_task', methods=['POST'])
def add_task():
    name = request.form['name']
    db.insert('task', name=name)
    return redirect('/')

@app.route('/edit_tasks', methods=['POST'])
def edit_tasks():
    print request.form.keys()
    if 'complete' in request.form:
        for key in request.form.keys():
            if key != 'complete':
                db.update('task', {'id': key, 'completed': True})
                # return redirect('/')
    elif 'delete' in request.form:
        for key in request.form.keys():
            if key != 'delete':
                db.delete('task', {'id': key})
                # return redirect('/')
    else:
        pass
    return redirect('/')



app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
