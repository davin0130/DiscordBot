import pymysql
# import psycopg2

get_all_user_sql = "SELECT id FROM user_info"

host = "localhost"
port = 3306
database = "tjdb"
username = "root"
password = "1234"

# Discord Bot Connection
def dbconn():
    conn = pymysql.connect(
        host=host,
        user=username,
        passwd=password,
        db=database,
        port=port,
        use_unicode=True,
        charset='utf8'
    )
    cursor = conn.cursor()
    result = cursor.execute(get_all_user_sql)
    conn.commit()
    
    return conn, cursor, result

conn, cursor, result = dbconn()

def dbclose():
    cursor.close()
    conn.close()



# print(conn)
# print(cursor)
# print(result)




# class DBConnection:
    
#     def __init__(self):
#         # connection = psycopg2.connect(
#         # host = 'dpg-ce6kvoen6mpk2bmk0db0-a.oregon-postgres.render.com',
#         # database = 'taejundb',
#         # user = 'taejun',
#         # password = 'PVLf75Wu9epD4MRQ9lG69NXa0Hw0eamE')

#         connection = psycopg2.connect(
#         host = 'localhost',
#         database = 'tjdb',
#         user = 'root',
#         password = '1234')

#         cursor = connection.cursor()
#         cursor.execute(get_all_user_sql)
#         result = str(cursor.fetchall())
#         print(len(result))
#         connection.commit()
#         return result

#     # get_user_info
#     def getAllUser():
#         cursor.execute(get_all_user_sql)
#         user_all_info = cursor.fetchall()
#         print(user_all_info)
#         return user_all_info

#     # get_user_info
#     def getUser(id):
#         cursor.execute(get_user_sql, id)
#         user_info = cursor.fetchall()
#         print(user_info)
#         return user_info