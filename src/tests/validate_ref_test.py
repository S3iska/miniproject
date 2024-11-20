import unittest
from entities.ref import Ref
from util import validate_ref, UserInputError

class TestRefValidation(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_article_ref_does_not_raise_error(self):
        validate_ref(
            Ref(None, 'article', 'ref_name', 'author', 'title', 1997, None)
        )