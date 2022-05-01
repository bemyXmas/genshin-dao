from sqlalchemy import Integer, Column, Text, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True)
    weapons_name = Column(Text(30))
    main_stat = Column(Text)
    sub_stat = Column(Text)
    stars = Column(Text)
    weapon_type = Column(Text, ForeignKey("characters.weapon_type"), nullable=False)

    def __repr__(self):
        return f"Weapon(id={self.id}, weapons_name={self.weapons_name}, main_stat={self.main_stat}, sub_stat={self.sub_stat}, stars={self.stars}, weapon_type={self.weapon_type})"
