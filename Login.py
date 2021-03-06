import sqlite3
import getpass

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS Users
    (id INTEGER PRIMARY KEY, Name TEXT, Username CHAR, Email CHAR, Password CHAR)''')

tables = cur.fetchall()

def AddEntry(Name,Username,Email,Password):
    cur.execute('''INSERT INTO Users (Name,Username,Email,Password)
    VALUES (?,?,?,?)''',(Name,Username,Email,Password))

def register():
    name = str(input("What's your name? "))
    username = input("Enter a username: ")
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    verfpassword = getpass.getpass("Enter your password again: ")

    while password != verfpassword:
        print("You must to enter the SAME password!")
        register()
        break

    cur.execute('SELECT * FROM Users WHERE Username = ? AND Email = ?', (username,email))

    if cur.fetchall():
        print("Your account is already created..")
        menu()
    
    else:
        print("Your account was create succefuly...")
        AddEntry(name, username, email, password)
        conn.commit()

    login()

def login():
    username1 = input("username: ")
    password1 = getpass.getpass("password: ")

    cur.execute('SELECT * FROM Users WHERE Username = ? AND Password = ?', (username1,password1))

    if cur.fetchall():
        print("Welcome " + "{" + username1 + "}" + " you are logged!")

    else:
        print("")
        print("Login Failed...")
        print("Maybe, your account is not created. Go to REGISTER to create a new account.")
        print("")
        menu()



def menu():
    response = str(input("Login(l) or Register(r): "))

    if response == "l":
        login()

    elif response == "r":
        register()

    else:
        print("Please enter either Login(l) or Register(r): ")
        menu()
menu()


