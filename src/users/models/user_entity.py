import uuid
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from decouple import config
from config.db import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("phone_number", sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("alias", sqlalchemy.String, unique=True, nullable=False),
)