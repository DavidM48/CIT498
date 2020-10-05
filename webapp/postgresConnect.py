import psycopg2



class dbconnect():

    def __init__(self):
        print("Created DB setup")
    
    def connectToDB(self):
        self.conn = psycopg2.connect(host="users.c7jggitb6poy.us-east-1.rds.amazonaws.com", database="users", user="postgres", password="postgres498")

    def insertUser(self, username, password, salt):
        sql = """INSERT INTO public."userTable"("userID", username, userpassword, usersalt)
                    VALUES (DEFAULT, %s, %s, %s);"""
        self.connectToDB()
        self.createCursor()
        try:
            self.cur.execute(sql,(username, password, salt))
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("INSERT Error: {}".format(error))
        finally:
            self.cur.close()
            self.closeDB()
    
    def setUser(self,username):
        self.username = username

    def getUserFromDB(self, username):
        sql = """SELECT username, userpassword, usersalt 
                    FROM public."userTable"
                    WHERE username = %s;"""
        result = None

        self.connectToDB()
        self.createCursor()
        
        try:
            self.cur.execute(sql, (username,))
            result = self.cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print("SELECT Error: {}".format(error))
        finally:
            self.cur.close()
            self.closeDB()

        return result

    def createCursor(self):
        self.cur = self.conn.cursor()
    
    def getUser(self):
        pass

    def closeDB(self):
        self.conn.close()