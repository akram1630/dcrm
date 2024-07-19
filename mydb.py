import mysql.connector 
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456',
)

#prepare curso object
cursorObject = dataBase.cursor()

#create database
#we can do it on workbench or shell cmd
cursorObject.execute("CREATE DATABASE elderco")
print('all done')
#after running this i have to do :
#python manage.py migrate
#after that i can delete this code