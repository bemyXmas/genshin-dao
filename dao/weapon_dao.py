from sqlalchemy.orm import Session
from models.weapon import Weapon


class WeaponDao:
    """DAO for weapon model."""

    def __init__(self, session: Session):
        self.__session = session

    def get_weapon(self):
        """Show all weapon."""
        return self.__session.query(Weapon).all()

    def get_weapon_by_id(self, id):
        """Get weapon by id."""
        try:
            return self.__session.query(Weapon).filter_by(id=id).first()
        except:
            print("There is no weapon with id" + id)
    
    def add_weapon(self, weapon: Weapon):
        """Add the weapon."""
        self.__session.add(weapon)
        self.__session.commit()
        print("Added weapon successfully!")
    
    def update_weapon_name(self, id, new_name):
        """Update weapon name query by ID"""
        try:
            find_weapon = self.__session.query(Weapon).filter_by(id=id).first()
            find_weapon.weapons_name  = new_name
            self.__session.commit()
            print("Update weapon name successfully!")
        except:
            print("There is no weapon with id" + id)
        
    def delete_weapon(self, id):
        """Delete weapon query by ID"""
        try:
            find_weapon = self.__session.query(Weapon).filter_by(id=id).first()
            self.__session.delete(find_weapon)
        except:
            print("There is no weapon with id" + id)



