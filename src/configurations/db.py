import databases
import sqlalchemy


DATABASE_URL = f"postgresql://postgres:mysecret@localhost:5432/movies"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()