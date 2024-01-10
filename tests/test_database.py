from database import Database


class TestDatabase:

    def test_existing_ingredients(self):
        new_database = Database()
        assert len(new_database.existing_ingredients()) == 6

    def test_existing_buns(self):
        new_database = Database()
        assert len(new_database.existing_buns()) == 3