import unittest
from services import doi
from entities.ref import Ref


class TestDoi(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_type(self):
        article = doi.parse_type("journal-article")
        self.assertEqual(article, "article")
        inproceedings = doi.parse_type("proceedings-article")
        self.assertEqual(inproceedings, "inproceedings")
        book = doi.parse_type("book")
        self.assertEqual(book, "book")
        other = doi.parse_type("abcd")
        self.assertEqual(other, "article")

    def test_parse_authors_returns_string_of_names(self):
        data = [{"given": "ABC", "family": "DEF"},
                {"given": "GHI", "family": "JKL"}]
        parsed = doi.parse_authors(data)
        self.assertEqual(parsed, "ABC DEF, GHI JKL")

    def test_parse_authors_returns_none_when_given_no_data(self):
        data = None
        parsed = doi.parse_authors(data)
        self.assertTrue(parsed is None)

    def test_parse_editors_returns_string_of_names(self):
        data = [{"given": "ABC", "family": "DEF"},
                {"given": "GHI", "family": "JKL"}]
        parsed = doi.parse_editors(data)
        self.assertEqual(parsed, "ABC DEF, GHI JKL")

    def test_parse_editors_returns_none_when_given_no_data(self):
        data = None
        parsed = doi.parse_editors(data)
        self.assertTrue(parsed is None)

    def test_parse_org_name_of_org(self):
        data = [{"name": "ABC"}]
        parsed = doi.parse_organization(data)
        self.assertEqual(parsed, "ABC")

    def test_parse_org_returns_none_when_given_no_data(self):
        data = None
        parsed = doi.parse_organization(data)
        self.assertTrue(parsed is None)

    def test_validate_doi_returns_true_with_valid_doi(self):
        self.assertTrue(doi.validate_doi("10.5555/12345678"))
        self.assertTrue(doi.validate_doi("10.1081/e-escs3"))
        self.assertTrue(doi.validate_doi("10.1115/HT2012-58597"))
        self.assertTrue(doi.validate_doi("10.1609/aaai.v38i1.27750"))

    def test_validate_doi_returns_false_with_invalid_prefix(self):
        self.assertFalse(doi.validate_doi("11.5555/12345678"))
        self.assertFalse(doi.validate_doi("10.a555/12345678"))

    def test_validate_doi_returns_false_with_invalid_suffix(self):
        self.assertFalse(doi.validate_doi("10.5555/12,345678"))
        self.assertFalse(doi.validate_doi("10.5555/12 345678"))

    def test_validate_doi_returns_false_with_empty_doi(self):
        self.assertFalse(doi.validate_doi(""))

    def test_get_ref_by_doi_returns_none_doi_is_invalid(self):
        self.assertTrue(doi.get_ref_by_doi("") is None)

    def test_get_ref_by_doi_returns_none_if_doi_is_not_indexed(self):
        self.assertTrue(doi.get_ref_by_doi("10.5555/1388398") is None)

    def test_get_ref_by_doi_returns_ref(self):
        self.assertIsInstance(doi.get_ref_by_doi("10.1081/e-escs3"), Ref)
