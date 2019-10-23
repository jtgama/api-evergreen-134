import mysql.connector as mysql
cnx = mysql.MySQLConnection(
    host="stevendb.mysql.database.azure.com",
    port= 3306,
    user= "Steven@stevendb",
    password= "@Itssomething",
    database="evergreen",
)
