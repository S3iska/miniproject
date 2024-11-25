from repositories.ref_repository import get_refs
import unittest
from unittest.mock import Mock
from entities.ref import Ref
from config import db
from sqlalchemy import text
from app import app


class TestRefRepo(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            self.mock_db = Mock()
            query = text("SELECT * FROM refs")
            mock_result = db.session.execute(query)
            self.mock_db.session.execute.return_value = mock_result

    def test_get_refs_calls_database(self):
        get_refs(self.mock_db)
        self.mock_db.session.execute.assert_called()

    def test_get_refs_returns_list_of_refs(self):
        result = get_refs(self.mock_db)
        self.assertTrue(type(result[0]), Ref)
