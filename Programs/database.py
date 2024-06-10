import sqlite3

def create_tables():
    tabA = sqlite3.connect("accounts.db")
    cursor = tabA.cursor()
    # Create a table to store user credentials
    cursor.execute('''CREATE TABLE IF NOT EXISTS trainees
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          firstname TEXT,
                          email TEXT,
                          password TEXT)''')
    tabA.close()

def user_search(user_email, user_password ):
    tabA = sqlite3.connect('accounts.db')
    cursor = tabA.execute('''SELECT email, password FROM trainees;''')
    for row in cursor:
        if row[0] == user_email and row[1] == user_password:
            return True
    return False

def add_user(first_name, email, hashed_pass):
    create_tables()
    tabA = sqlite3.connect("accounts.db")
    cursor = tabA.cursor()
    cursor.execute("INSERT OR IGNORE INTO trainees (email, password, first_name) VALUES (?, ?, ?)",
                   (email, hashed_pass, first_name))
    tabA.commit()

if __name__ == '__main__':
    print(add_user('john',  'john@sfc.uk.co', "pass" ))