import sqlite3
import re
import random
conn= sqlite3.connect("Banking.db")
c=conn.cursor()

def createTable():
  c.execute('CREATE TABLE IF NOT EXISTs userData(username TEXT,contact REAL,acc_no text, email TEXT,cash int(1000), password TEXT NOT NULL PRIMARY KEY)')

def dataEntry():
    username = input("enter your username: ")
    contact = input("enter your contact number: ")
    match = re.match(r'[789]\d{9}$',contact)
    while match == None:
        print("contact number is invalid..")
        contact = input("enter your contact number: ")
        match = re.match(r'[789]\d{9}$',contact)

    a="1922"
    for i in range(8):
        a=a+str(int(random.random()*10))
    print("acc no is:",a)
    city=input("enter your city: ")
    pincode=input("enter your pincode: ")
    match = re.match(r'[789]\d{9}$',pincode)


    email = input("enter your mail ID: ")
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    while match == None:
        print('enter a valid mail address..')
        email = input("enter your mail ID: ")
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    password = input("enter your password: ")
    cnfPassword = input("re-enter your password: ")

    if password == cnfPassword:
        cash=0
        c.execute("INSERT INTO userData VALUES (?,?,?,?,?,?)",(username, contact,a,email,cash, password))
        print("Registration successful!")
    else:
        print("passwords did not match.")

    conn.commit()
    c.close()
    conn.close()
createTable()
#dataEntry()
