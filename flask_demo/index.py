# import mysql.connector
# import xlrd

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="jit@12345",
#     database="website"
# )

# mycursor = mydb.cursor()

# loc = "C:\\Flask\\Flask6\\flask_demo\\uploads\\mobile.csv"

# l = list()
# a = xlrd.open_workbook(loc)
# sheet = a.sheet_by_index(0)

# for i in range(1, sheet.nrows):
#     l.append(tuple(sheet.row_values(i)))

# sql = "INSERT INTO mobiles (name, ratings, price, imgURL, corpus) VALUES (%s, %s, %s, %s, %s)"

# # Inserting all rows at once using executemany
# mycursor.executemany(sql, l)
# mydb.commit()
# mydb.close()
