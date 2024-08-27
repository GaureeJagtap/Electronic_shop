from flask import Flask, render_template, request, jsonify
import mysql.connector as connection

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('signup.html')


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        mydb = connection.connect(host="localhost", database="website", user="root", password="jit@12345")
        cursor = mydb.cursor()
        result = ''
        print(request.form)

        cursor.execute("insert into operations values({}, {}, {})".format(username, email, password))
        mydb.commit()
        try:
            if connection.is_connected():
                result = "Connection Established.."
                connection.close()
            else:
                print("Connection Failed..")
        except mysql.connector.Error as error:
            print(error)

        return render_template('signup.html', result=result)
    else:
        return jsonify({'error': 'Missing form data keys'}),


@app.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        mydb = connection.connect(host="localhost", database="website", user="root", password="jit@12345")
        cursor = mydb.cursor()
        result = ''
        print(request.json)

        cursor.execute("insert into operations values({}, {}, {})".format(username, email, password))
        mydb.commit()
        try:
            if connection.is_connected():
                result = "Connection Established.."
                connection.close()
            else:
                print("Connection Failed..")
        except mysql.connector.Error as error:
            print(error)

        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid request method'}),


if __name__ == '__main__':
    app.run()
