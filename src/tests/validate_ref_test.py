from copy import copy
import unittest
from entities.ref import Ref
from util import UserInputError

class TestRefValidation(unittest.TestCase):
    def setUp(self):
        self.valid_article = Ref(
            id = None,
            ref_type = "article",
            ref_name = "REF65",
            author = "Test author",
            title = "Test title",
            year = 1997,
            journal = "Test journal"
        )

        self.valid_inproceedings = Ref(
            id = None,
            ref_type = "inproceedings",
            ref_name = "REF65",
            author = "Test author",
            booktitle = "Test booktitle",
            year = 1997,
            publisher = "Test publisher"
        )

    def test_valid_article_ref_does_not_raise_error(self):
        self.valid_article.validate()
    
    def test_valid_inproceedings_ref_does_not_raise_error(self):
        self.valid_inproceedings.validate()
    
    def test_missing_or_invalid_ref_type_raises_error(self):
        ref = copy(self.valid_article)

        ref.ref_type = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.ref_type = "something"
        with self.assertRaises(UserInputError):
            ref.validate()
    
    def test_missing_or_too_long_ref_name_raises_error(self):
        ref = copy(self.valid_article)

        ref.ref_name = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.ref_name = "a"*101
        with self.assertRaises(UserInputError):
            ref.validate()

    def test_missing_or_too_short_or_long_author_raises_error(self):
        ref = copy(self.valid_article)

        ref.author = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.author = "a"*2
        with self.assertRaises(UserInputError):
            ref.validate()

        ref.author = "a"*101
        with self.assertRaises(UserInputError):
            ref.validate()
    
    def test_missing_or_too_short_or_long_title_raises_error(self):
        ref = copy(self.valid_article)

        ref.title = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.title = "a"*2
        with self.assertRaises(UserInputError):
            ref.validate()

        ref.title = "a"*251
        with self.assertRaises(UserInputError):
            ref.validate()
    
    def test_missing_or_too_short_or_long_booktitle_raises_error(self):
        ref = copy(self.valid_inproceedings)

        ref.booktitle = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.booktitle = "a"*2
        with self.assertRaises(UserInputError):
            ref.validate()

        ref.booktitle = "a"*251
        with self.assertRaises(UserInputError):
            ref.validate()
    
    def test_missing_or_too_short_or_long_journal_raises_error(self):
        ref = copy(self.valid_article)

        ref.journal = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.journal = "a"*2
        with self.assertRaises(UserInputError):
            ref.validate()

        ref.journal = "a"*251
        with self.assertRaises(UserInputError):
            ref.validate()
    
    def test_missing_or_too_short_or_long_publisher_raises_error(self):
        ref = copy(self.valid_inproceedings)

        ref.publisher = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.publisher = "a"*2
        with self.assertRaises(UserInputError):
            ref.validate()

        ref.publisher = "a"*251
        with self.assertRaises(UserInputError):
            ref.validate()

    def test_missing_or_invalid_year_raises_error(self):
        ref = copy(self.valid_article)

        ref.year = None
        with self.assertRaises(UserInputError):
            ref.validate()
        
        ref.year = 1599
        with self.assertRaises(UserInputError):
            ref.validate()

        ref.year = 2101
        with self.assertRaises(UserInputError):
            ref.validate()
