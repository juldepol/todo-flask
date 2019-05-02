from sqlite3 import Error

class Task:
    def __init__(self, conn):
        self.conn = conn

    def list(self):
        try:
            query = "SELECT * FROM task"
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return rows 
        except Error as e:
            print(e)
            return e    

    def add(self, task):
        try: 
            query = 'INSERT INTO "task" VALUES (NULL, ?, 0)'
            cur = self.conn.cursor()
            cur.execute(query, [task])   
        except Error as e:
            print(e)
            return e  

    def complete(self, id):
        try:
            query = "UPDATE task SET done=1 WHERE task.id = ?"
            cur = self.conn.cursor()
            cur.execute(query, [id]) 
        except Error as e:
            print(e) 
            return e 

    def delete(self, id):
        try:
            query = "DELETE FROM task WHERE task.id = ?"
            cur = self.conn.cursor()
            cur.execute(query, [id]) 
        except Error as e:
            print(e)  
            return e