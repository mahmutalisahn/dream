import os

# Postgre settings
user_name = os.getenv("POSTGRE_USER")
password = os.getenv("POSTGRE_PASSWORD")
url = os.getenv("POSTGRE_URL")
port = os.getenv("POSTGRE_PORT")
dbname = os.getenv("POSTGRE_DBNAME")
 
print(user_name, password, url, port, dbname)