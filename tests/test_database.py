from praktikum_files.database import Database

def test_get_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) > 0


def test_get_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) > 0
