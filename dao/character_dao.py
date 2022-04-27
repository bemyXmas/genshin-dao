from sqlalchemy.orm import Session

class CharacterDao:
    """DAO for character model."""

    def __init__(self, session: Session):
        self.__session = session

    def get_
