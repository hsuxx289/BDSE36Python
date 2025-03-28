import pymysql


class SqlQuery:


    def __init__(self, database=None):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )


    def show_db(self):
        with self.connection.cursor() as cursor:
            sql = "SHOW DATABASES;"
            cursor.execute(sql)
            result = cursor.fetchall()
        
        return result



    def show_table(self):
        with self.connection.cursor() as cursor:
            sql = "SHOW TABLES;"
            cursor.execute(sql)
            result = cursor.fetchall()
        
        return result
    
    def query(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        
        return result
    
if __name__ == "__main__":
    q = SqlQuery()
    dbs = q.show_db()

    print(dbs)