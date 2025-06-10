from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here


class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = Column()
    magnitude = Column()
    location = Column()
    year = Column()

    def __repr__(self):
        return f"Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}"
