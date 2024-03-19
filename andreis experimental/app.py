
#======================================================
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database file path (update this with your actual database file)
DB_FILE = "animals.db"

# GET request to retrieve all animals from the 'animals' table
@app.route("/animals/all", methods=["GET"])
def get_animals():
    """show all animals in the animals DB
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animals")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/animals/2adopt", methods=["GET"])
def get_animals_awaiting_adoption():
    """show all animals in the animals DB that have no current owner and that are waiting to be adopted
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM animals WHERE owner IS NULL")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/animals/age/<int:min_age>,<int:max_age>", methods=["GET"])
def get_by_age_range(min_age=0, max_age=100):
    """show all animals in the animals DB that have age matching the search
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM animals WHERE age BETWEEN {min_age} AND {max_age}")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/animals/<species>", methods=["GET"])
def get_by_species(species):
    """show all animals of the matching species
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM animals WHERE species = '{species}'")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/animals/<breed>", methods=["GET"])
def get_by_breed(breed):
    """show all animals of the matching breed
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM animals WHERE breed = '{breed}'")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/animals/<name>", methods=["GET"])
def get_by_name(name):
    """show the animals with the matching name
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM animals WHERE name = '{name}'")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/animals/<chip_number>", methods=["GET"])
def get_by_chip_number(chip_number):
    """show the animal with the matching chip number
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM animals WHERE chip_number = '{chip_number}'")
        animals = cursor.fetchall()
        conn.close()
        return jsonify(animals)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

# GET request to retrieve all column names from the 'animals' table
@app.route("/animals/searchCategories", methods=["GET"])
def get_animalsColumnsNames():
    """ this is needed to know what categories can be used for searching the DB
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info(animals)")
        columns = cursor.fetchall()
        conn.close()
        return jsonify([col[1] for col in columns])  # Extract column names
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


# Configure your database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adoption.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your database model
class Adoption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contract_date = db.Column(db.String(20), nullable=False)
    contract_location = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the database tables
db.create_all()

# Define the route for /submitAdoption endpoint
@app.route('/submitAdoption', methods=['POST'])
def submit_adoption():
    data = request.json
    contract_date = data.get('contractDate')
    contract_location = data.get('contractLocation')
    name = data.get('name')
    age = data.get('age')
    address = data.get('address')
    phone = data.get('phone')
    email = data.get('email')

    adoption = Adoption(contract_date=contract_date, contract_location=contract_location,
                        name=name, age=age, address=address, phone=phone, email=email)

    db.session.add(adoption)
    db.session.commit()

    return jsonify({"message": "Adoption application submitted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)