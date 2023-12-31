import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, name TEXT, surname TEXT, age TEXT, photo TEXT)""")

    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()


async def edit_profile(data, user_id):
        cur.execute("""
        UPDATE profile SET name = '{}', surname = '{}', age = '{}', photo = '{}' WHERE user_id == '{}'""".format(
            data['name'], data['surname'], data['age'], data['photo'], user_id))
        db.commit()
