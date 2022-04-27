from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    characters_name = Column(Text(30))
    stars = Column(Text)
    weapon_type = Column(Text)

    def __repr__(self):
        return f"Character(id={self.id}, characters_name={self.characters_name}, stars={self.stars}, weapon_type={self.weapon_type})"
