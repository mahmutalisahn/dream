from sqlalchemy import create_engine

connection_url = f"postgresql://cqbmsisnpozims:9402e3fb09aa82a658d550112857164733910c6cfb328ad428c759a9132fd94e@ec2-34-242-8-97.eu-west-1.compute.amazonaws.com/dbhhbl2m1sggau"
sqlalchemy_engine = create_engine(connection_url)