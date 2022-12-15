import sqlite3
import time

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, referall_id=None):
        with self.connection:
            if referall_id !=None:
                return self.cursor.execute('INSERT INTO "users" ("user_id", "referal_id") VALUES (?, ?)', (user_id, referall_id,))

            else:
                return self.cursor.execute('INSERT INTO "users" ("user_id") VALUES (?)', (user_id,))




    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            return bool(len(result))

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute('UPDATE "users" SET "nickname" = ? WHERE "user_id" = ?',(nickname, user_id,))

    def get_signup(self, user_id):
        
        with self.connection:
            result = self.cursor.execute('SELECT "signup" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            # result =  self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            for row in result:
                signup =str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute('UPDATE "users" SET "signup" = ? WHERE "user_id" = ?', (signup, user_id,))

    def get_nickname(self, user_id):
        
        with self.connection:
            result = self.cursor.execute('SELECT "nickname" FROM "users" WHERE "user_id" = ?', ( user_id,)).fetchall()
            # result =  self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            for row in result:
                nickname =str(row[0])
            return nickname

   

    def set_time_sub (self, user_id, tarif):
        with self.connection:
            return self.cursor.execute('UPDATE "users" SET "time_sub" = ? WHERE "user_id" = ?', (tarif, user_id,))

    def get_time_sub(self, user_id):

        with self.connection:
            result = self.cursor.execute(
                'SELECT "time_sub" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            # result =  self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            return time_sub

    def get_sub_status(self, user_id):

        with self.connection:
            result = self.cursor.execute(
                'SELECT "time_sub" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            # result =  self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            if time_sub> int(time.time()):
                return True
            else:
                return False

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute('UPDATE "users" SET "active" = ? WHERE "user_id" = ?', (active, user_id,))

    def get_users_smm(self):
        with self.connection:
            return self.cursor.execute('SELECT "user_id","active" FROM "users"').fetchall()

 # def get_tarif (self, user_id,):
    #     with self.connection:
    #         result = self.cursor.execute('SELECT "time_sub" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
    #         for row in result:
    #             tarif = row[0]
    #         return tarif

    def set_ref(self, user_id):
        with self.connection:
            result1 = self.cursor.execute('SELECT "count_ref" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchone()
            for row in result1:
                result1 = row
            result1 = result1 +1
            self.cursor.execute('UPDATE "users" SET "count_ref" = ? WHERE "user_id" = ?', (result1, user_id,))
            result = self.cursor.execute('SELECT "ref_free" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            for row in result:
                result = int(row[0])
            result = result +1
            self.cursor.execute('UPDATE "users" SET "ref_free" = ? WHERE "user_id" = ?', (result, user_id,))

    def minus_ref(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT "ref_free" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            for row in result:
                result = int(row[0])
            result = result -1
            self.cursor.execute('UPDATE "users" SET "ref_free" = ? WHERE "user_id" = ?', (result, user_id,))

    def get_free(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT "ref_free" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            for row in result:
                result = int(row[0])
            return result

    def get_referal(self, user_id):
        with self.connection:
            result1 = self.cursor.execute('SELECT "count_ref" FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            for row in result1:
                result1 = int(row[0])
            return result1

    def num_krug(self, k):
        with self.connection:
            result = self.cursor.execute('SELECT "num_krug" FROM "users" WHERE "user_id" = ?', (k,)).fetchone()
            result = result[0] + 1
            self.cursor.execute('UPDATE "users" SET "num_krug" = ? WHERE "user_id" = ?', (result, k,))
            return result
