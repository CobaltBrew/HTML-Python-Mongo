from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data from request
    name = request.form['name']
    email = request.form['email']

    # Insert data into MongoDB
    collection.insert_one({'name': name, 'email': email})

    # Return a success message
    return jsonify({'message': 'Form submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)