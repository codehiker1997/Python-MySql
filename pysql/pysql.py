# This is the practice to work with sql in python and i can do it fairly

# First we will install sql connector in python by using the following pip command (python -m pip install mysql-connector-python)
# First of all import mysql connector 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",

)

print(mydb)
