import unittest
from entities.tag import Tag, validate_tag, UserInputError


class TestTag(unittest.TestCase):
    def test_validate_accepts_good_tag(self):
        tag = Tag(1, "abc")
        validate_tag(tag)

    def test_validate_fails_tag_with_too_short_name(self):
        tag = Tag(1, "ab")
        try:
            validate_tag(tag)
            self.fail()
        except UserInputError:
            self.assertTrue(True)

    def test_validate_fails_tag_without_name(self):
        tag = Tag(1, None)
        try:
            validate_tag(tag)
            self.fail()
        except UserInputError:
            self.assertTrue(True)

    def test_validate_fails_tag_with_invalid_name(self):
        tag = Tag(1, "@bc")
        try:
            validate_tag(tag)
            self.fail()
        except UserInputError:
            self.assertTrue(True)
