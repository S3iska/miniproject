from dataclasses import dataclass, fields
from util import UserInputError, validate_string

@dataclass
class Ref:
    id: int = None
    ref_type: str = None
    ref_name: str = None

    author: str = None
    title: str = None
    journal: str = None
    year: int = None
    volume: str = None
    pages: str = None
    month: str = None
    doi: str = None
    note: str = None
    key: str = None

    publisher: str = None
    series: str = None
    address: str = None
    edition: str = None
    url: str = None

    booktitle: str = None
    editor: str = None
    organization: str = None

    def get_bibtex(self):
        field_blacklist = ["id", "ref_type", "ref_name"]

        res = f"@{self.ref_type}{{{self.ref_name},\n"
        for field in fields(self):
            if field.name in field_blacklist:
                continue

            value = getattr(self, field.name)
            if value is not None:
                res += f"    {field.name} = {{{value}}},\n"
        res += "}"
        return res


    def validate(self):
        if self.ref_type not in ["article", "book", "inproceedings"]:
            raise UserInputError("Reference type is missing or invalid.")

        validate_string(self.ref_name, "Reference name", False, 1, 100)
        validate_string(self.author, "Author", False, 3, 100)

        if self.ref_type == "inproceedings":
            validate_string(self.booktitle, "Book title", False, 3, 250)
        else:
            validate_string(self.title, "Title", False, 3, 250)

        if self.ref_type == "article":
            validate_string(self.journal, "Journal", False, 3, 250)
        else:
            validate_string(self.publisher, "Publisher", False, 3, 250)

        if not (self.year and 1600 < self.year < 2100):
            raise UserInputError("Year must be between 1600 and 2100")

        validate_string(self.volume, "Volume", True, 1, 250)
        validate_string(self.pages, "Pages", True, 1, 250)
        validate_string(self.month, "Month", True, 1, 250)
        validate_string(self.doi, "DOI", True, 1, 250)
        validate_string(self.note, "Note", True, 1, 250)
        validate_string(self.key, "Key", True, 1, 250)
        validate_string(self.series, "Series", True, 1, 250)
        validate_string(self.address, "Address", True, 1, 250)
        validate_string(self.edition, "Edition", True, 1, 250)
        validate_string(self.url, "URL", True, 1, 250)
        validate_string(self.editor, "Editor", True, 1, 250)
        validate_string(self.organization, "Organization", True, 1, 250)
