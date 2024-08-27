from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector as connection

app = Flask(__name__)


def is_user_exists(username, email, cursor):
    # Check if the username or email already exists in the database
    cursor.execute("SELECT * FROM signup WHERE username = %s OR email = %s", (username, email))
    return cursor.fetchone() is not None


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    if request.method == 'POST':
        return redirect(url_for('login_page'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        return redirect(url_for('homepage'))
    return render_template('login.html')


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('page1.html')


@app.route('/cart.html')
def cart_html():  # Renamed to avoid conflict
    return render_template('cart.html')


@app.route('/related_items')
def related_items():
    # You can perform any logic here before rendering the related_items.html page
    return render_template('related_items.html')

@app.route('/signup', methods=['POST'])  # This will be called from UI
def signuppage():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        result = ''
        print(request.form)
        try:
            mydb = connection.connect(host="localhost", database="website", user="root", password="j@gt@pg@uri#210704")
            cursor = mydb.cursor()
            result = ''

            # Check if the user already exists
            if is_user_exists(username, email, cursor):
                result = "User with this username or email already exists. Please enter another information."
            else:
                # Insert the new user
                cursor.execute("INSERT INTO signup VALUES (%s, %s, %s)", (username, email, password))
                mydb.commit()
                result = "Account created successfully."

            if mydb.is_connected():
                mydb.close()
            else:
                print("Connection Failed..")
        except Exception as e:
            print(f"Error: {e}")

    return render_template('page1.html', result=result)


@app.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOAPUI
def signuppage_via_postman():
    if request.method == 'POST':
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        result = ''
        print(request.json)
        try:
            mydb = connection.connect(host="localhost", database="website", user="root", password="j@gt@pg@uri#210704")
            cursor = mydb.cursor()
            result = ''

            # Check if the user already exists
            if is_user_exists(username, email, cursor):
                result = "User with this username or email already exists. Please enter another information."
            else:
                # Insert the new user
                cursor.execute("INSERT INTO signup VALUES (%s, %s, %s)", (username, email, password))
                mydb.commit()
                result = "Account created successfully."

            if mydb.is_connected():
                mydb.close()
            else:
                print("Connection Failed..")
        except Exception as e:
            print(f"Error: {e}")

        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
