from sqlalchemy import create_engine
from config_manager import dbname, password, url, user_name

connection_url = f"postgresql://{user_name}:{password}@{url}/{dbname}"
print(connection_url)
sqlalchemy_engine = create_engine(connection_url)