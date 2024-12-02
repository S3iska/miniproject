from dataclasses import dataclass, fields

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
