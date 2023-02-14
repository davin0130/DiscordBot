import TJ_DBConnection

conn, cursor, result = TJ_DBConnection.dbconn()

# user_sql
select_all_user_sql  = "SELECT * FROM user_info LIMIT 0, 20"
select_id_user_sql   = "SELECT * FROM user_info WHERE user_id=%s"
insert_user_sql      = "INSERT INTO user_info(user_id, tag, join_date) VALUES(%s, %s, %s)"
select_admin_sql     = "SELECT * FROM user_info WHERE admin=1"

# chat_sql
select_all_chat_sql  = "SELECT * FROM chat_info LIMIT 0, 20"
select_id_chat_sql   = "SELECT * FROM chat_info WHERE user_id=%s and channel=%s"
insert_chat_sql      = "INSERT INTO chat_info(user_id, channel, in_time) VALUES(%s, %s, %s)"
update_chat_sql      = "UPDATE chat_info SET out_time=%s where user_id=%s and channel=%s"

# voice_sql
select_all_voice_sql  = "SELECT * FROM voice_info LIMIT 0, 20"
select_id_voice_sql   = "SELECT * FROM voice_info WHERE user_id=%s and channel=%s"
insert_voice_sql      = "INSERT INTO voice_info(user_id, channel, in_time) VALUES(%s, %s, %s)"
update_voice_sql      = "UPDATE voice_info SET out_time=%s where user_id=%s and channel=%s"
reset_voice_sql       = "UPDATE voice_info SET in_time=%s, out_time=null where user_id=%s and channel=%s"


# =================================================================

class User:
    # select_all_chat DISTINCT 20
    def selectAllUser():   
        cursor.execute(select_all_chat_sql)
        cursor.fetchall()
        conn.commit()

    # select_user per id
    def selectIDUser(user_id):
        cursor.execute(select_id_chat_sql, user_id)
        user_id_info = cursor.fetchall()
        conn.commit()
        return user_id_info

    # insert_user_sql(Intime From Channel)
    def insertUser(user_id, tag, current_time):
        value = (user_id, tag, current_time)
        cursor.execute(insert_user_sql, value)
        cursor.fetchall()
        conn.commit()
    
    # select_admin
    def searchAdmin():
        cursor.execute(select_admin_sql)
        admin_list = cursor.fetchall()
        conn.commit()
        return admin_list


# =================================================================

class Chat:
    # select_all_chat DISTINCT 20
    def selectAllChat():   
        cursor.execute(select_all_chat_sql)
        cursor.fetchall()
        conn.commit()

    # select_chat per id
    def selectIDChat(user_id, channel):
        value = (user_id, channel)
        cursor.execute(select_id_chat_sql, value)
        chat_id_info = cursor.fetchall()
        conn.commit()
        return chat_id_info

    # insert_chat_sql(Intime From Channel)
    def insertChat(user_id, channel, current_time):
        value = (user_id, channel, current_time)
        cursor.execute(insert_chat_sql, value)
        cursor.fetchall()
        conn.commit()

    # update_chat_sql(Outtime From Channel)
    def updateChat(current_time, user_id, channel):
        value = (current_time, user_id, channel)
        cursor.execute(update_chat_sql, value)
        cursor.fetchall()
        conn.commit()

# =================================================================

class Voice:
    # select_all_voice DISTINCT 20
    def selectAllVoice():   
        cursor.execute(select_all_voice_sql)
        cursor.fetchall()
        conn.commit()

    # select_voice per id
    def selectIDVoice(user_id, channel):
        value = (user_id, channel)
        cursor.execute(select_id_voice_sql, value)
        voice_id_info = cursor.fetchall()
        conn.commit()
        return voice_id_info

    # insert_voice_sql(Intime From Channel)
    def insertVoice(user_id, channel, current_time):
        value = (user_id, channel, current_time)
        cursor.execute(insert_voice_sql, value)
        cursor.fetchall()
        conn.commit()

    # update_voice_sql(Outtime From Channel)
    def updateVoice(current_time, user_id, channel):
        value = (current_time, user_id, channel)
        cursor.execute(update_voice_sql, value)
        cursor.fetchall()
        conn.commit()
    
    # reset_voice_sql
    def resetVoice(current_time, user_id, channel):
        value = (current_time, user_id, channel)
        cursor.execute(reset_voice_sql, value)
        cursor.fetchall()
        conn.commit()
