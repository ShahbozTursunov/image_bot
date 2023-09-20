import sqlite3 as sql

import datetime

from datetime import date

from datetime import timedelta

async def create_table():
    with sql.connect("users.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                    user_id BIGINT,
                    username TEXT,
                    create_date TEXT
                    )""")


async def create_user(user_id, username, create_date):
    with sql.connect("users.db") as con:
        cur = con.cursor()

        user = cur.execute("""SELECT user_id FROM users WHERE user_id = ?""", (user_id,)).fetchone()
        # fetchone()
        # fetchall()
        # fetchmany(5)
        
        if user is None:
            cur.execute("""
            INSERT INTO users (user_id, username, create_date) VALUES (?, ?, ?)
            """, (user_id, username, create_date))


async def select_all_users():
    with sql.connect("users.db") as con:
        cur = con.cursor()

        users = cur.execute("SELECT count(user_id) FROM users").fetchone()
        return users[0]


async def select_today_users():
    with sql.connect("users.db") as con:
        cur = con.cursor()

        users = cur.execute("SELECT create_date FROM users").fetchall()
        counter = 0
        for user in users:        
            user_date = datetime.datetime.strptime(user[0], "%Y-%m-%d %H:%M")
            if user_date.day == datetime.datetime.now().day:
                print("Today")
                counter += 1
        return counter
    
# async def select_yesterday_users():
#     with sql.connect("users.db") as con:
#         cur = con.cursor()

#         users = cur.execute("SELECT create_date FROM users").fetchall()
#         counter = 0
#         for user in users:
#             today = date.today()
#             user_date = datetime.datetime.strptime(user[0], "%Y-%m-%d %H:%M")
#             if user_date.day == today - timedelta(days = 1):

#                 print(user)
#                 counter += 1
#         return counter

async def select_yesterday_users():
    with sql.connect("users.db") as con:
        cur = con.cursor()
        users = cur.execute("SELECT create_date FROM users").fetchall()
        counter = 0

        for user in users:
            today = date.today()
            user_date = datetime.datetime.strptime(user[0], "%Y-%m-%d %H:%M")
            if user_date.day == (datetime.datetime.now() - datetime.timedelta(days=1)).day:

                print(user)
                counter += 1
        return counter
    
async def get_all_users():
    with sql.connect("users.db") as con:
        cur = con.cursor()

        users = cur.execute("""SELECT user_id FROM users""").fetchall()
        return users 