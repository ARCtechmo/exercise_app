# Exercise Databasse App
import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS exercise(
            date TEXT,
            year INTEGER,
            month INTEGER,
            miles INTEGER
            ) ''')

def show_all():
    with conn:
        cur.execute("SELECT rowid, * FROM exercise")
        items = cur.fetchall()
        for item in items:
            print(item)

def add_many(exercise_log):
    with conn:
        cur.executemany("INSERT INTO exercise VALUES(?,?,?,?)",(exercise_log))
        conn.commit()

def add_one(exercise_log):
    with conn:
        cur.execute("INSERT INTO exercise VALUES(?,?,?,?)",(exercise_log))
        conn.commit()

def delete_one(id):
    with conn:
        cur.execute("DELETE FROM exercise WHERE rowid=?",(id, ))
        conn.commit()
