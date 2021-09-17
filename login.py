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
        if(self.check_if_username_exists(username, database) == False):
            print('Username is not registred.')
            return
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



if __name__ == '__main__':
    os.system('cls')
    Login()