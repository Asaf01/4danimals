from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add_applicant.html')

@app.route('/add_applicant', methods=['POST'])
def add_applicant():
    if request.method == 'POST':
        # Get form data
        full_name = request.form['full_name']
        teudat_zehut = request.form['teudat_zehut']
        address = request.form['address']
        city = request.form['city']
        email = request.form['email']
        phone = request.form['phone']
        approved = True if 'approved' in request.form else False
        owner_of = request.form['owner_of']

        # Connect to the database
        conn = sqlite3.connect('animal_shelter.db')
        c = conn.cursor()

        # Insert data into Applicants table
        c.execute('''INSERT INTO Applicants 
                     (full_name, teudat_zehut, address, city, mail, phone, approved, owner_of) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                     (full_name, teudat_zehut, address, city, email, phone, approved, owner_of))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
