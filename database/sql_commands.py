import sqlite3
from database import sql_queries



class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_VOICE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_users(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
(None, telegram_id, username, first_name, last_name)
        )
        self.connection.commit()

    def sql_inserts_poll_votes(self, telegram_id, answer):
        self.cursor.execute(
            sql_queries.INSERT_VOICE_QUERY,
(telegram_id, answer)
        )

        self.connection.commit()

    def sql_inserts_ban_list(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_list(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USERS_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_update_ban_user_count(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_insert_user_form_register(self, telegram_id, nickname, biography, geolocation,
                                      gender, age, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, biography, geolocation, gender, age, photo,)
        )
        self.connection.commit()





