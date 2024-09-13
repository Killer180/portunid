import csv
import sqlite3
from datetime import datetime

# this "learned_words" is for test only.
learned_words = ['abandon', 'ability', 'able', 'abnormal']

def import_new_words (filename):
    conn = sqlite3.connect('vocabulary_hs.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vocabulary_hs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        english TEXT NOT NULL UNIQUE,
        chinese TEXT,
        practice_times INTEGER NOT NULL DEFAULT 0,
        last_practice_date TEXT
        )
    ''')

    with open(filename, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        to_db = [(row['english'], row['chinese'], row['practice_times'], row['last_practice_date']) for row in csv_reader]

    cursor.executemany("INSERT OR IGNORE INTO vocabulary_hs (english, chinese, practice_times, last_practice_date) VALUES (?, ?, ?, ?);", to_db)

    conn.commit()

# verify the database
    cursor.execute("SELECT * FROM vocabulary_hs")
    print(cursor.fetchall())
    print('the data is growing up!')

    conn.close()


def update_practice_data ():
    conn = sqlite3.connect('vocabulary_hs.db')
    cursor = conn.cursor()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for word in learned_words:
        cursor.execute('''
        UPDATE vocabulary_hs
        SET practice_times = practice_times + 1,
            last_practice_date = ?
        WHERE english = ?
        ''', (current_time,word))

    conn.commit()
    print(current_time)

    # verify the database
    cursor.execute("SELECT * FROM vocabulary_hs")
    print(cursor.fetchall())
    print('we updated the data!')

    conn.close()

# clear up the current database in need.
def clear_up_db ():
    conn = sqlite3.connect('vocabulary_hs.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM vocabulary_hs")

    #Reset the AUTOINCREMENT counter - id will restart from 1"
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='vocabulary_hs'")

    conn.commit()

    # verify the database
    cursor.execute("SELECT * FROM vocabulary_hs")
    print(cursor.fetchall())
    print('the database is clean now!')
    cursor.close()
    conn.close()



print(learned_words)

update_practice_data()
 