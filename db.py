import mysql.connector


mydb = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7352566",
    password="5lW5yi4np2",
    database="sql7352566"
)


def read_all():
    print("Reading from DB")
    c = mydb.cursor()
    c.execute("SELECT * FROM groups")
    print(c.fetchall())

def find(userid, branch):
    print("Find method")
    c = mydb.cursor()
    c.execute(f"SELECT * FROM groups WHERE userid='{userid}' AND branch='{branch}'")
    print("Done")
    return list(c)


def add(Auserid, Abranch, Afilename):
    print("Add method")
    c = mydb.cursor()
    c.execute(f"""INSERT INTO groups (userid, branch, filename)
VALUES ('{Auserid}', '{Abranch}', '{Afilename}');""")
    mydb.commit()
    print("Done")


if __name__ == "__main__":
    read_all()
    add('430437500.0', '%test1', 'test1.jpg')
    read_all()