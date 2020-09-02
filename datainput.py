import sqlite3 
import time 
import sys 


conn = sqlite3.connect('C:\\Users\\me\\Documents\\Python\\Information Database\\Datainfo.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Datainfo (password,username,information)''')

conn.commit()

# This function is asking for a user what they want to do wheter create a new file or open an existing one 
def ask_for_input():
    global command_input
    print("Welcome to data sending data program where you can create new files that can be viewed later on.")
    command_input = input("Select'c' or 'v' to creating a file or viewing a file!")
    command = command_input
    while command == 'c' and command == 'v':
            command_input = input("Make sure that you select either 'c' or 'v' for creating a file or viewing a file!")

    if command == 'c':
        print('OK...Lets create a file!')
    else:
        print('OK... Lets view an exsiting file!')



def sign_in():
    global username
    global password
    global password_input 
    global username_input
    global information
    global information_input
    global sign_in

    print("Welcome to Datainfo, you will need to create a username and password in order to use this service.")
    username_input = input("What do you want to make your username?")
    username = username_input
    while username_input == '':
        username_input = input("Invalid Input! What do you want to make your username?") 

    
    password_input = input("What do you want to set your password as? Remember that you can not change your password!: ")
    check_for_password = input('Please re-enter your password to confirm: ')
    password = password_input
    while check_for_password != password:
        password_input = input("What do you want to set your password as? Remember that you can not change your password!:")

    information_input = input("What information do you want to store!")
    information = information_input
    while information == '':
         information_input = input("Invalid Input! What information do you want to store!")

    cur.execute("INSERT INTO Datainfo VALUES('dev21','DevParikh','I like to eat food haha')")
    cur.execute("INSERT INTO Datainfo  VALUES('john31','johndoe','Whats up ')")
    cur.execute("INSERT INTO Datainfo VALUES('avengersinfinitywar','avengers','avergers go!')")
    cur.execute("INSERT INTO Datainfo VALUES('ironman27','mrstark','stark industries')")
    conn.commit()
    cur.execute("SELECT rowid FROM Datainfo WHERE username = (?)", (username_input,))
    conn.commit()
    data = cur.fetchall()

    if len(data) != 0:
        print("Hi {}, you have already logged into Datainfo!".format(username_input))
        sign_in = True
        time.sleep(2)
        sys.exit()



def gathering_data():
    global userQuery
    username_input = input("What is your username?")
    cur.execute("SELECT rowid FROM Datainfo WHERE username = (?)", (username_input,))
    username_data = cur.fetchall()

    if len(username_input) == 0:
        print("You are not signed up for Datainfo, goodbye!")
        time.sleep(3)
        sys.exit()
    
    trypassword = input("Enter your password!")
    
    cur.execute("SELECT password FROM Datainfo WHERE username = (?)", (username_input,))
    password_data = cur.fetchall()[0][0]

    while password_data != trypassword:
        trypassword = input("Incorrect Password! Enter your password!\n")


    
    cur.execute("SELECT information, password, username FROM Datainfo WHERE username = (?)", (username_input,))
    userQuery = cur.fetchall()
def viewing_info():
    gathering_data()

    print("Okay... here is your data!")
    print("Here is your information,", userQuery[0][0])
    sys.exit()

def creating_users():
    cur.execute("INSERT INTO Datainfo VALUES (?,?,?)", (password_input, username_input,information_input,))
    conn.commit()


ask_for_input()
if command_input == 'c':
    sign_in()
    creating_users()

elif command_input == 'v':
    viewing_info()
else:
    print("An error has occured!")
    sys.exit()


