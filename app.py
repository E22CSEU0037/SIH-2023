from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('mongodb+srv://geetika056349singh:pwskills@cluster0.fnthsgd.mongodb.net/?retryWrites=true&w=majority')
db = client['odopj&k']
collection = db['signup']






# # Configure the collectionDB connection URI
# app.config["collection_URI"] = "collectiondb://localhost:27017/myDatabase"

# # Initialize Pycollection
# collection = Pycollection(app)

@app.route('/')
def index():
    return render_template('account.html')

@app.route('/account', methods=['POST'])
def signup():
    username = request.form['txt']
    email = request.form['email']
    password = request.form['pswd']

    # Insert the user data into the collectionDB "inventory" collection
    inventory = collection.db.inventory
    inventory.insert_one({'username': username, 'email': email, 'password': password})

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['pswd']

    # Find the user in the collectionDB "inventory" collection
    inventory = collection.db.inventory
    user = inventory.find_one({'email': email, 'password': password})

    if user:
        return redirect(url_for('dashboard'))
    else:
        return "Login failed. Invalid email or password."

@app.route('/dashboard')
def dashboard():
    # This route corresponds to the dashboard page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)