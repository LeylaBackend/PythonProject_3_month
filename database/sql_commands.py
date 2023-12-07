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
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_USERS_TABLE_QUERY)

        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USER_V2_TABLE)
        except sqlite3.OperationalError:
            pass

        self.connection.execute(sql_queries.CREATE_TABLE_ASYNC)
        self.connection.commit()

    def sql_insert_users(self, telegram_id, username, first_name, last_name):
        try:
            self.cursor.execute(
                sql_queries.INSERT_USER_QUERY,
                (None, telegram_id, username, first_name, last_name, None, None,)
            )
        except sqlite3.IntegrityError:
            pass
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
            sql_queries.SELECT_BAN_USER_QUERY,
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

    def sql_select_user_form(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "geolocation": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_all_user_form(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "geolocation": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7]
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_FORM_QUERY,
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker)
        )
        self.connection.commit()

    def sql_select_filter_user_form(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "geo": row[4],
            "gender": row[5],
            "age": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_select_balance_count_referral(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "count": row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_reference_link(self, link, owner):
        self.cursor.execute(
            sql_queries.UPDATE_REFERENCE_LINK_QUERY,
            (link, owner,)
        )
        self.connection.commit()

    def sql_select_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "link": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_LINK_QUERY,
            (telegram_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "tg_id": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_update_balance(self, tg_id):
        print(tg_id)
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_referral(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral,)
        )
        self.connection.commit()

    def sql_insert_referral_users(self, owner, common_users, user_name, first_name):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_USERS_QUERY,
            (None, owner, common_users, user_name, first_name)
        )
        self.connection.commit()

    def sql_select_referral_users(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "owner_id": row[1],
            "custom_id": row[2],
            "user_name": row[3],
            "first_name": row[4]
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERRAL_USERS_QUERY,
            (owner,)
        ).fetchall()

    def sql_insert_service_commands(self, link):
        self.cursor.execute(
            sql_queries.INSERT_ASYNC,
            (None,link)
        )
        self.connection.commit()