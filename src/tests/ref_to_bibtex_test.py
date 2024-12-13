from copy import copy
import unittest
from entities.ref import Ref

class TestRefToBibtex(unittest.TestCase):
    def test_bibtex_is_correct_full_article(self):
        ref = Ref(
            id = None,
            ref_type = "article",
            ref_name = "REF65",
            author = "test author",
            title = "test title",
            year = 1997,
            journal = "test journal",
            volume = "4",
            pages = "241-245",
            month = "6",
            doi = "10.1000/182",
            note = "test note",
            key = "test key"
        )

        correct_bibtex = ("@article{REF65,\n"
                          "    author = {test author},\n"
                          "    title = {test title},\n"
                          "    journal = {test journal},\n"
                          "    year = {1997},\n"
                          "    volume = {4},\n"
                          "    pages = {241-245},\n"
                          "    month = {6},\n"
                          "    doi = {10.1000/182},\n"
                          "    note = {test note},\n"
                          "    key = {test key},\n"
                          "}")

        bibtex = ref.get_bibtex()
        self.assertEqual(bibtex, correct_bibtex)
    

    def test_bibtex_is_correct_full_book(self):
        ref = Ref(
            id = None,
            ref_type = "book",
            ref_name = "REF65",
            author = "test author",
            title = "test title",
            year = 1997,
            publisher = "test publisher",
            volume = "4",
            month = "6",
            note = "test note",
            key = "test key",
            series = "test series",
            address = "test address",
            edition = "test edition",
            url = "https://www.google.com"
        )

        correct_bibtex = ("@book{REF65,\n"
                          "    author = {test author},\n"
                          "    title = {test title},\n"
                          "    year = {1997},\n"
                          "    volume = {4},\n"
                          "    month = {6},\n"
                          "    note = {test note},\n"
                          "    key = {test key},\n"
                          "    publisher = {test publisher},\n"
                          "    series = {test series},\n"
                          "    address = {test address},\n"
                          "    edition = {test edition},\n"
                          "    url = {https://www.google.com},\n"
                          "}")

        bibtex = ref.get_bibtex()
        self.assertEqual(bibtex, correct_bibtex)
    
    def test_bibtex_is_correct_full_inproceedings(self):
        ref = Ref(
            id = None,
            ref_type = "inproceedings",
            ref_name = "REF65",
            author = "test author",
            title = "test title",
            year = 1997,
            booktitle = "test book title",
            publisher = "test publisher",
            volume = "4",
            pages = "242-245",
            month = "6",
            note = "test note",
            key = "test key",
            series = "test series",
            address = "test address",
            editor = "test editor",
            organization = "test organization"
        )

        correct_bibtex = ("@inproceedings{REF65,\n"
                          "    author = {test author},\n"
                          "    title = {test title},\n"
                          "    year = {1997},\n"
                          "    volume = {4},\n"
                          "    pages = {242-245},\n"
                          "    month = {6},\n"
                          "    note = {test note},\n"
                          "    key = {test key},\n"
                          "    publisher = {test publisher},\n"
                          "    series = {test series},\n"
                          "    address = {test address},\n"
                          "    booktitle = {test book title},\n"
                          "    editor = {test editor},\n"
                          "    organization = {test organization},\n"
                          "}")

        bibtex = ref.get_bibtex()
        self.assertEqual(bibtex, correct_bibtex)
    
    def test_bibtex_is_correct_optional_fields_missing(self):
        ref = Ref(
            id = None,
            ref_type = "article",
            ref_name = "REF65",
            author = "test author",
            title = "test title",
            year = 1997,
            journal = "test journal"
        )

        correct_bibtex = ("@article{REF65,\n"
                          "    author = {test author},\n"
                          "    title = {test title},\n"
                          "    journal = {test journal},\n"
                          "    year = {1997},\n"
                          "}")

        bibtex = ref.get_bibtex()
        self.assertEqual(bibtex, correct_bibtex)