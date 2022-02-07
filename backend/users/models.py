from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(
        String, unique=True, nullable=False
    )
    username = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
