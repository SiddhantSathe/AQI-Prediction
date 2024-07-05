import mindsdb_sdk
import MySQLdb


try:
    con = mindsdb_sdk.connect('http://127.0.0.1:47334')
    print('Connected to MindsDB')
except Exception as e:
    print('Error connecting to MindsDB:', e)
    con = None

# Get a list of databases
databases = con.databases.list()
print('Databases:', databases)

#create a database
db = con.databases.create('aqi')
print('Database created:', db)




# connect mysql database to mindsdb
# try:
#     db = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="root@123",db="aqi")
#     print('Connected to MySQL')
# except Exception as e:
#     print('Error connecting to MySQL:', e)
#     db = None











