from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def admin_page():
    return render_template('admin.html')

@app.route('/show_volunteers')
def show_volunteers():
    conn = sqlite3.connect('animal_shelter.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Volunteers")
    volunteers = c.fetchall()
    conn.close()
    return render_template('show_table.html', table_name='Volunteers', entries=volunteers)

@app.route('/show_applicants')
def show_applicants():
    conn = sqlite3.connect('animal_shelter.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Applicants")
    applicants = c.fetchall()
    conn.close()
    return render_template('show_table.html', table_name='Applicants', entries=applicants)

@app.route('/show_animals')
def show_animals():
    conn = sqlite3.connect('animal_shelter.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Animal")
    animals = c.fetchall()
    conn.close()
    return render_template('show_table.html', table_name='Animal', entries=animals)

@app.route('/delete_entry', methods=['POST'])
def delete_entry():
    if request.method == 'POST':
        table = request.form['table']
        entry_id = request.form['entry_id']
        
        conn = sqlite3.connect('animal_shelter.db')
        c = conn.cursor()
        
        c.execute(f"DELETE FROM {table} WHERE id=?", (entry_id,))
        
        conn.commit()
        conn.close()
        
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
