import os
import sqlite3

class Login():
    def __init__(self):
        if(os.path.isfile('./database.db')):
            database = sqlite3.connect('database.db')
        else:
            database = sqlite3.connect('database.db')
            self.create_database(database)
        username = input('Enter your username:\n> ')
        while(self.check_if_username_exists(username, database) == False):
            print('Username is not registred.')
            want_register = input('Would you like to create an account? (yes or no)\n> ')
            if(want_register == 'yes','y'):
                self.create_user(username, database)
                username = input('Enter your username:\n> ')
            elif(want_register == 'no','n'):
                username = input('Enter your username:\n> ')
            else:
                want_register = input('Would you like to create an account? (yes or no)\n> ')
        password = input('Enter your password:\n> ')
        while(self.check_password(username, password, database) == False):
            print('Invalid password.')
            password = input('Enter your password:\n> ')
        else:
            print('Logged in!')
    def create_database(self, database):
        cursor = database.cursor()
        cursor.execute('CREATE TABLE users (username text, password text)')
        cursor.close()
    def check_if_username_exists(self, username, database):
        cursor = database.cursor()
        cursor.execute('SELECT username FROM users WHERE username = \'{}\''.format(username))
        check = cursor.fetchall()
        cursor.close()
        if len(check)==0:
            return False
        else:
            return True
    def check_password(self, username, password, database):
        cursor = database.cursor()
        cursor.execute('SELECT password FROM users WHERE username = \'{}\''.format(username))
        stored_password = cursor.fetchall()
        if(stored_password[0][0] == password):
            return True
        else:
            return False
    def create_user(self, username, database):
        cursor = database.cursor()
        password = input('Choose your password\n> ')
        confirm_password = input('Repeat your password\n> ')
        while(password != confirm_password):
            print('Passwords do not match. Try again.')
            password = input('Choose your password:\n> ')
            confirm_password = input('Repeat your password:\n> ')
        cursor.execute('INSERT INTO users VALUES (\'{}\', \'{}\')'.format(username, password))
        cursor.close()
        print('User registred! Please log in.')



if __name__ == '__main__':
    os.system('cls')
    Login()