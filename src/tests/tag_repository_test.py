from repositories.tag_repository import get_tags, create_tag
import unittest
from unittest.mock import Mock
from entities.tag import Tag
from config import db
from sqlalchemy import text
from app import app
from db_helper import setup_db


class TestTagRepo(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            setup_db()
            self.mock_db = Mock()
            query = text("SELECT * FROM tags")
            mock_result = db.session.execute(query)
            self.mock_db.session.execute.return_value = mock_result

    def test_get_tags_calls_database(self):
        get_tags(self.mock_db)
        self.mock_db.session.execute.assert_called()

    def test_get_tags_returns_list_of_refs(self):
        result = get_tags(self.mock_db)
        self.assertTrue(type(result[0]), Tag)

    def test_create_tag_commits_if_adding_succeeds(self):
        create_tag(self.mock_db, Tag(1, "abc"))
        self.mock_db.session.commit.assert_called()

    def test_create_tag_rollbacks_if_adding_fails(self):
        self.mock_db.session.execute.side_effect = Exception('Test')
        try:
            create_tag(self.mock_db, Tag(1, "abc"))
        except Exception as e:
            self.assertTrue('Test' in e.args)
            self.mock_db.session.rollback.assert_called()
