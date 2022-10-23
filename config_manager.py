import os

# Postgre settings
user_name = os.getenv("POSTGRE_USER", "cqbmsisnpozims")
password = os.getenv("POSTGRE_PASSWORD", "9402e3fb09aa82a658d550112857164733910c6cfb328ad428c759a9132fd94e")
url = os.getenv("POSTGRE_URL", "ec2-34-242-8-97.eu-west-1.compute.amazonaws.com")
port = os.getenv("POSTGRE_PORT")
dbname = os.getenv("POSTGRE_DBNAME", "dbhhbl2m1sggau")
 
print(user_name, password, url, port, dbname)