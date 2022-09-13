from sqlalchemy import create_engine

connection_url = f"postgresql://user:password@localhost:5432/lapcalendar"
sqlalchemy_engine = create_engine(connection_url)