import random

from praktikum_files.bun import Bun
from praktikum_files.database import Database


def test_get_bun_name_returns_value():
    db = Database()
    bun = random.choice(db.available_buns())
    bun_name_from_db = bun.name
    bun_name = bun.get_name()
    assert bun_name == bun_name_from_db

def test_get_bun_price_returns_value():
    db = Database()
    bun = random.choice(db.available_buns())
    bun_price_from_db = bun.price
    bun_price = bun.get_price()
    assert bun_price == bun_price_from_db



