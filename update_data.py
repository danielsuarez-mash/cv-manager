import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# get latest CSVs
users = pd.read_csv("data/users.csv")
engagements = pd.read_csv("data/engagements.csv")
experiences = pd.read_csv("data/experiences.csv")

tables = {"users": users, "engagements": engagements, "experiences": experiences}

# # connect to postgres
# conn = psycopg2.connect(
#     dbname="cv_manager",
#     user="cvuser",
#     password="cvpassword",
#     host="localhost",
#     port='5432'
# )

# Define the database URL
DATABASE_URL = "postgresql://cvuser:cvpassword@localhost:5432/cv_manager"

# Create the SQLAlchemy engine
db = create_engine(DATABASE_URL)

with db.begin() as conn:
    # users.to_sql(name="users", con=conn, index=False, if_exists="replace")

    for table_name, table in tables.items():
        table.to_sql(name=table_name, con=conn, if_exists="replace")


