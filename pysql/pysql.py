# This is the practice to work with sql in python and i can do it fairly

# First we will install sql connector in python by using the following pip command (python -m pip install mysql-connector-python)
# First of all import mysql connector 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234567890F",
    database = "thisdata"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
# This is used to create the database table
# mycursor.execute("CREATE TABLE employees (name VARCHAR(255), address VARCHAR(255))")
mydb.commit()
print(mycursor.rowcount, 'row inserted')

mycursor.execute("SELECT * FROM students")

my_results = mycursor.fetchall()
for x in my_results:
    print(x)