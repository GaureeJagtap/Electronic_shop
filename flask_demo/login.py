from flask import Flask, render_template, request, jsonify
import mysql.connector as connection

login = Flask(__name__)


@login.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('login.html')


@login.route('/math', methods=['POST'])  # This will be called from UI
def loginpage():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = ''
        print(request.form)
        try:
            mydb = connection.connect(host="localhost", database="website", user="root", password="jit@12345")
            cursor = mydb.cursor()
            result = ''

            cursor.execute("insert into login values(%s, %s)", (email, password))
            mydb.commit()
            if mydb.is_connected():
                result = "Connection Established.."
                mydb.close()
            else:
                print("Connection Failed..")
        except Exception as e:
            print(f"Error: {e}")

    return render_template('login.html', result=result)


@login.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOAPUI
def loginpage_via_postman():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        result = ''
        print(request.json)
        try:
            mydb = connection.connect(host="localhost", database="website", user="root", password="jit@12345")
            cursor = mydb.cursor()
            result = ''

            cursor.execute("insert into login values(%s, %s)", (email, password))
            mydb.commit()

            if mydb.is_connected():
                result = "Connection Established.."
                mydb.close()
            else:
                print("Connection Failed..")
        except Exception as e:
            print(f"Error: {e}")

        return jsonify(result)


if __name__ == '__main__':
    login.run()
