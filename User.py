import discord
import TJ_DBConnection

db = TJ_DBConnection.DBConnection.dbconn()

get_all_user_sql = "SELECT id FROM user_info"
get_user_sql     = "SELECT * FROM user_info WHERE id = %s"

class User:
    # get_user_info
    def getAllUser():
        db.cursor.execute(get_all_user_sql)
        user_all_info = db.cursor.fetchall()
        print(user_all_info)
        return user_all_info

    # get_user_info
    def getUser(id):
        db.cursor.execute(get_user_sql, id)
        user_info = db.cursor.fetchall()
        print(user_info)
        return user_info