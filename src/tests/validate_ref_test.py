from copy import copy
import unittest
from entities.ref import Ref
from util import validate_ref, UserInputError

class TestRefValidation(unittest.TestCase):
    def setUp(self):
        self.valid_ref = Ref(
            id = None,
            ref_type = "article",
            ref_name = "REF65",
            author = "test author",
            title = "test title",
            year = 1997,
            publisher = "test publisher"
        )

    def test_valid_ref_does_not_raise_error(self):
        validate_ref(self.valid_ref)
    
    def test_missing_or_invalid_ref_type_raises_error(self):
        ref = copy(self.valid_ref)

        ref.ref_type = None
        with self.assertRaises(UserInputError):
            validate_ref(ref)
        
        ref.ref_type = "something"
        with self.assertRaises(UserInputError):
            validate_ref(ref)
    
    def test_missing_or_too_long_ref_name_raises_error(self):
        ref = copy(self.valid_ref)

        ref.ref_name = None
        with self.assertRaises(UserInputError):
            validate_ref(ref)
        
        ref.ref_name = "a"*101
        with self.assertRaises(UserInputError):
            validate_ref(ref)

    def test_not_alphanumeric_ref_name_raises_error(self):
        ref = copy(self.valid_ref)

        ref.ref_name = "ref name"
        with self.assertRaises(UserInputError):
            validate_ref(ref)

    def test_missing_or_too_short_or_long_author_raises_error(self):
        ref = copy(self.valid_ref)

        ref.author = None
        with self.assertRaises(UserInputError):
            validate_ref(ref)
        
        ref.author = "a"*2
        with self.assertRaises(UserInputError):
            validate_ref(ref)

        ref.author = "a"*101
        with self.assertRaises(UserInputError):
            validate_ref(ref)
    
    def test_missing_or_too_short_or_long_title_raises_error(self):
        ref = copy(self.valid_ref)

        ref.author = None
        with self.assertRaises(UserInputError):
            validate_ref(ref)
        
        ref.author = "a"*2
        with self.assertRaises(UserInputError):
            validate_ref(ref)

        ref.author = "a"*251
        with self.assertRaises(UserInputError):
            validate_ref(ref)
    
    def test_missing_or_invalid_year_raises_error(self):
        ref = copy(self.valid_ref)

        ref.year = None
        with self.assertRaises(UserInputError):
            validate_ref(ref)
        
        ref.year = 1600
        with self.assertRaises(UserInputError):
            validate_ref(ref)

        ref.year = 2100
        with self.assertRaises(UserInputError):
            validate_ref(ref)
    
    def test_missing_publisher_does_not_raise_error(self):
        ref = copy(self.valid_ref)

        ref.publisher = None
        validate_ref(ref)