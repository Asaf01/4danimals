from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add_animal.html')

@app.route('/add_animal', methods=['POST'])
def add_animal():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        color = request.form['color']
        birth_date = request.form['birth_date']
        age = request.form['age']
        species = request.form['species']
        brade_name = request.form['brade_name']
        chip_number = request.form['chip_number']
        spayed_neutered = True if 'spayed_neutered' in request.form else False
        arrival = request.form['arrival']
        foster = True if 'foster' in request.form else False
        current_owner = request.form['current_owner']
        vaccines = request.form['vaccines']

        # Connect to the database
        conn = sqlite3.connect('animal_shelter.db')
        c = conn.cursor()

        # Insert data into Animal table
        c.execute('''INSERT INTO Animal 
                     (name, color, birth_date, age, species, brade_name, chip_number, spayed_neutered, 
                     arrival, foster, current_owner, Vaccines) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                     (name, color, birth_date, age, species, brade_name, chip_number, spayed_neutered, 
                     arrival, foster, current_owner, vaccines))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
