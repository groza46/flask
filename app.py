from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import datetime

app = Flask(__name__)

# Initialize TinyDB (this will create a db.json file in your project directory)
db = TinyDB('db.json')
Event = Query()

@app.route('/')
def index():
    # Fetch all events from the database
    events = db.all()
    return render_template('index.html', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_desc = request.form['event_desc']

        # Convert the string date to a datetime object
        try:
            event_date = datetime.datetime.strptime(event_date, '%Y-%m-%d')
        except ValueError:
            return "Invalid date format. Use YYYY-MM-DD."

        # Insert the event into the database
        db.insert({
            'event_name': event_name,
            'event_date': event_date.strftime('%Y-%m-%d'),  # Store as string
            'event_desc': event_desc
        })
        return redirect(url_for('index'))
    return render_template('add_event.html')

@app.route('/delete/<int:event_id>', methods=['GET', 'POST'])
def delete_event(event_id):
    # Remove the event with the given ID from the database
    db.remove(doc_ids=[event_id])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
