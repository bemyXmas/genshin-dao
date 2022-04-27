from genshin import Genshin

genshin_db = Genshin.get_instance()


character_dao = genshin_db.get_character_dao()
weapon_dao = genshin_db.get_weapon_dao()

print(character_dao.get_characters())
