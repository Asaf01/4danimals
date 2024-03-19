import sqlite3
from faker import Faker
import random
import datetime

# Initialize Faker to generate fake data
fake = Faker()

def generate_animal_data():
    # Generate random animal data
    animal_data = []
    for _ in range(10):
        animal_data.append((
            fake.name(),
            fake.color(),
            fake.date_of_birth(minimum_age=1, maximum_age=15),
            random.uniform(0.5, 15.0),
            fake.word(),
            fake.word(),
            random.randint(100000000, 999999999),
            random.choice([True, False]),
            fake.date_this_year(),
            random.choice([True, False]),
            random.randint(1, 10),
            fake.word()
        ))
    return animal_data

def generate_breed_data():
    # Generate random breed data
    breed_data = []
    for _ in range(10):
        breed_data.append((
            fake.word(),
            random.choice([True, False])
        ))
    return breed_data

def generate_applicant_data():
    # Generate random applicant data
    applicant_data = []
    for _ in range(10):
        applicant_data.append((
            fake.name(),
            fake.random_number(digits=9),
            fake.address(),
            fake.city(),
            fake.email(),
            fake.phone_number(),
            random.choice([True, False]),
            fake.word()
        ))
    return applicant_data

def populate_database():
    # Connect to the database
    conn = sqlite3.connect('animal_shelter.db')
    c = conn.cursor()

    # Generate and insert data into Animal table
    animal_data = generate_animal_data()
    c.executemany('INSERT INTO Animal VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)', animal_data)

    # Generate and insert data into Breeds table
    breed_data = generate_breed_data()
    c.executemany('INSERT INTO Breeds VALUES (?,?)', breed_data)

    # Generate and insert data into Applicants table
    applicant_data = generate_applicant_data()
    c.executemany('INSERT INTO Applicants VALUES (NULL,?,?,?,?,?,?,?,?)', applicant_data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Call the function to populate the database
populate_database()
