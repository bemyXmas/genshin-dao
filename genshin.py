from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.character_dao import CharacterDao
from dao.weapon_dao import WeaponDao

class Genshin:

    character_dao = None
    weapon_dao = None

    def __init__(self, connection_url="sqlite:///genshin-data.db"):
        engine = create_engine(connection_url)
        Session = sessionmaker(bind=engine)
        self.__db_session = Session()
    
    def get_character_dao(self):
        """Get character dao."""
        if self.character_dao is None:
            self.character_dao = CharacterDao(session=self.__db_session)
        return self.character_dao
    
    def get_weapon_dao(self):
        """Get weapon dao."""
        if self.weapon_dao is None:
            self.weapon_dao = WeaponDao(session=self.__db_session)
        return self.weapon_dao
    
    def close_db(self):
        """Close all the database"""
        self.__db_session.close()