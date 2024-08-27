from flask import Flask, render_template, request, redirect, url_for, jsonify

import mysql.connector

app = Flask(__name__)
app.config['TEMPLATE_FOLDER'] = 'C:\Flask\Flask6 7\flask_demo\templates'

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "jit@12345",
    "database": "website"
}


# Function to fetch all products from the database
def get_all_products():
    try:
        # Establish a connection and create a cursor
        mydb = mysql.connector.connect(**db_config)
        mycursor = mydb.cursor()

        # Fetch all products from the database
        query = "SELECT name, ratings, price, imgURL, corpus FROM website.mobile"
        mycursor.execute(query)
        results = mycursor.fetchall()

        # Close the cursor and the database connection
        mycursor.close()
        mydb.close()

        # Convert the results to a list of dictionaries
        products = [
            {'name': result[0], 'ratings': result[1], 'price': result[2],
             'imgURL': result[3], 'corpus': result[4]}
            for result in results
        ]

        return products

    except Exception as e:
        print(f"Error: {e}")
        return []

# Flask route to fetch all products
@app.route('/get_all_products', methods=['GET'])
def get_all_products_route():
    products = get_all_products()
    return jsonify({'products': products})


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


@app.route('/signup', methods=['POST'])
def signuppage():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        result = ''

        try:
            # Establish a connection and create a cursor
            mydb = mysql.connector.connect(host="localhost", database="website", user="root", password="jit@12345")
            mycursor = mydb.cursor()

            # Check if the user already exists
            if is_user_exists(username, email, mycursor):
                result = "User with this username or email already exists. Please enter another information."
            else:
                # Insert the new user
                mycursor.execute("INSERT INTO signup VALUES (%s, %s, %s)", (username, email, password))
                mydb.commit()
                result = "Account created successfully."

            # Close the cursor and the database connection
            mycursor.close()
            mydb.close()

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
            mydb = connection.connect(host="localhost", database="website", user="root", password="jit@12345")
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



@app.route('/search', methods=['GET'])
def search_product():
    if request.method == 'GET':
        search_query = request.args.get('query')

        # Establish a connection and create a cursor
        mydb = mysql.connector.connect(**db_config)
        mycursor = mydb.cursor()

        try:
            # Search for the product in the database based on the user's query
            query = "SELECT name, price, imgURL, corpus FROM website.mobile WHERE name LIKE %s OR corpus LIKE %s"
            mycursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
            results = mycursor.fetchall()

            # Convert the results to a list of dictionaries
            products = [{'name': result[0], 'price': result[1], 'imgURL': result[2], 'corpus': result[3]} for result in results]

            # Close the cursor and the database connection
            mycursor.close()
            mydb.close()

            return jsonify({'products': products})

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': 'An error occurred while processing the request'})



@app.route('/process_buy_request', methods=['POST'])
def process_buy_request():
    # Placeholder logic, update as needed
    product_name = request.form.get('product_name')
    quantity = request.form.get('quantity')
    address = request.form.get('address')
    payment_mode = request.form.get('payment_mode')

    # Perform any necessary processing with the form data
    # (e.g., save to database, perform payment processing, etc.)

    # For demonstration purposes, just redirect to the buy.html page
    return redirect(url_for('buy_html'))


# @app.route('/buy.html')
# def buy_html():  # Renamed to avoid conflict
#     # Assuming you have a function to fetch product details, 
#     # you need to call that function and pass the product data to the template
#     product = {'name': name, 'price': price, 'imgURL': imgURL, 'corpus': corpus}
#     return render_template('buy.html', product=product)

@app.route('/buy.html')
def buy_html():
    try:
        # Assuming you have a function to fetch product details
        product_details = get_product_details()  # Call your function here

        # Extract product details
        name = product_details['name']
        price = product_details['price']
        imgURL = product_details['imgURL']
        corpus = product_details['corpus']

        # Create a dictionary with product details
        product = {'name': name, 'price': price, 'imgURL': imgURL, 'corpus': corpus}

        # Pass product details to the template
        return render_template('buy.html', product=product)

    except Exception as e:
        print(f"Error: {e}")
        # Handle the error gracefully, maybe render an error page
        return render_template('error.html')

@app.route('/cart.html')
def cart_html():  # Renamed to avoid conflict
    return render_template('cart.html')


@app.route('/categories.html')
def categories():  # Renamed to avoid conflict
    return render_template('categories.html')


@app.route('/account.html')
def account():  # Renamed to avoid conflict
    return render_template('account.html')


if __name__ == '__main__':
    app.run(debug=True)
