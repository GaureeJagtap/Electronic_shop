from flask import Flask, render_template, request, jsonify
import mysql.connector as connection

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])      # To render Homepage
def home_page():
    return render_template('index.html')



@app.route('/math', methods=['POST'])      # This will be called from UI
def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':

            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 + num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the sum of '+str(num1)+' and '+str(num2) + ' is '+str(r)
        if operation == 'subtract':

            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 - num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 * num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':

            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 / num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)


@app.route('/via_postman', methods=['POST'])       # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 + num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'subtract':

            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 - num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':

            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 * num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            try:
                mydb = connection.connect(host="localhost", database="addition", user="root",
                                          password="j@gt@pg@uri#210704")
                cursor = mydb.cursor()
                r = num1 / num2
                cursor.execute("insert into operations values({}, {}, {})".format(num1, num2, r))
                mydb.commit()
            except Exception as e:
                print(f"Error: {e}")
        result = 'the division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


if __name__ == '__main__':
    app.run()
