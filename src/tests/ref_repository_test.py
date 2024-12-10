from repositories.ref_repository import get_refs
import unittest
from unittest.mock import Mock
from entities.ref import Ref
from config import db
from sqlalchemy import text
from app import app
from db_helper import setup_db


class TestRefRepo(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            setup_db()
            self.mock_db = Mock()
            query = text("""
                SELECT *, array_agg(t.tag_name) as tags
                FROM refs r
                LEFT JOIN ref_tags rt ON r.id = rt.ref_id
                LEFT JOIN tags t ON rt.tag_id = t.tag_id
                GROUP BY r.id, rt.ref_id, rt.tag_id, t.tag_id
            """)
            mock_result = db.session.execute(query)
            self.mock_db.session.execute.return_value = mock_result

    def test_get_refs_calls_database(self):
        get_refs(self.mock_db)
        self.mock_db.session.execute.assert_called()

    def test_get_refs_returns_list_of_refs(self):
        result = get_refs(self.mock_db)
        self.assertTrue(type(result[0]), Ref)
