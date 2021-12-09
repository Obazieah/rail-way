import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'railway_net',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS customers(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        address VARCHAR(355) NOT NULL,
        PRIMARY KEY(ID)
    )
    """
)

mycursor.execute(
      """CREATE TABLE IF NOT EXISTS delists(
        ID INT NOT NULL AUTO_INCREMENT,
        traveller_name VARCHAR(255),
        from_where VARCHAR(255),
        to_where VARCHAR(255),
        departure_time INT,
        PRIMARY KEY(ID)
    )
    """
)
mycursor.execute(
     """CREATE TABLE IF NOT EXISTS checks(
        ID INT NOT NULL AUTO_INCREMENT,
        traveller_name VARCHAR(255),
        from_text VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)