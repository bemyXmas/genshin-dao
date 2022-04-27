from sqlalchemy.orm import Session
from models.character import Character

class CharacterDao:
    """DAO for character model."""

    def __init__(self, session: Session):
        self.__session = session

    def get_characters(self):
        """Show all Character."""
        return self.__session.query(Character).all()

    def get_character_by_id(self, id):
        """Get character by id."""
        try:
            return self.__session.query(Character).filter_by(id=id).first()
        except:
            print("There is no character with id" + id)
    
    def add_character(self, character: Character):
        """Add the character."""
        self.__session.add(character)
        self.__session.commit()
        print("Added Character successfully!")
    
    def update_character_name(self, id, new_name):
        """Update character name query by ID"""
        try:
            find_char = self.__session.query(Character).filter_by(id=id).first()
            find_char.characters_name  = new_name
            self.__session.commit()
            print("Update Character name successfully!")
        except:
            print("There is no character with id" + id)
        
    def delete_character(self, id):
        """Delete character query by ID"""
        try:
            find_char = self.__session.query(Character).filter_by(id=id).first()
            self.__session.delete(find_char)
        except:
            print("There is no character with id" + id)



