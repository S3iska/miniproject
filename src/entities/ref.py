from dataclasses import dataclass, fields

class UserInputError(Exception):
    pass

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

    def _validate_article(self):
        if not self.author:
            raise UserInputError("Author field is required.")
        if not 3 <= len(self.author) <= 100:
            raise UserInputError(
                "Author name must be between 3 and 100 characters long"
            )

        if not self.title:
            raise UserInputError("Title field is required.")
        if not 3 <= len(self.title) <= 250:
            raise UserInputError(
                "Title must be between 3 and 250 characters long"
            )

        if not self.year:
            raise UserInputError("Year field is required.")
        if not 1600 < self.year < 2100:
            raise UserInputError("Year must be between 1600 and 2100")

    def validate(self):
        if not self.ref_type:
            raise UserInputError("Reference type is required.")

        if not self.ref_name:
            raise UserInputError("Reference name is required.")
        if not len(self.ref_name) <= 100:
            raise UserInputError(
                "Reference name must be less than 100 characters long."
            )
        if not self.ref_name.isalnum():
            raise UserInputError(
                "Refrerence name must only contain letters and numbers"
            )

        if self.ref_type == "article":
            self._validate_article()
        else:
            raise UserInputError("Invalid reference type.")
