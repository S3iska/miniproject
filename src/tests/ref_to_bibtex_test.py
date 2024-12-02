from copy import copy
import unittest
from entities.ref import Ref
from util import validate_ref, UserInputError

class TestRefToBibtex(unittest.TestCase):
    def setUp(self):
        self.ref = Ref(
            id = None,
            ref_type = "article",
            ref_name = "REF65",
            author = "test author",
            title = "test title",
            year = 1997
        )

    def test_bibtex_is_correct(self):
        correct_bibtex = ("@article{REF65,\n"
                          "    author = {test author},\n"
                          "    title = {test title},\n"
                          "    year = {1997},\n"
                          "}")

        bibtex = self.ref.get_bibtex()
        self.assertEqual(bibtex, correct_bibtex)