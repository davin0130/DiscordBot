import discord
import psycopg2

# Discord Bot Connection
class DBConnection:
    
    def __init__(self):
        connection = psycopg2.connect(
        host = 'dpg-ce6kvoen6mpk2bmk0db0-a.oregon-postgres.render.com',
        database = 'taejundb',
        user = 'taejun',
        password = 'PVLf75Wu9epD4MRQ9lG69NXa0Hw0eamE')

        cursor = connection.cursor()

        print(cursor)
        cursor.execute("select * from public.text_info limit 10 offset 10")

        rows = cursor.fetchall()

        
        connection.commit()


# Discord Bot Connection
