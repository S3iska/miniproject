from string import ascii_letters
from requests import get, Timeout
from entities.ref import Ref


def get_ref_by_doi(doi_id):
    if not validate_doi(doi_id):
        return None
    response = get(f"https://api.crossref.org/works/{doi_id}", timeout=3)
    if response is Timeout:
        return None
    if response.status_code == 404:
        return None
    data = response.json()
    ref_data: dict = data.get("message")
    # print(ref_data)
    new_ref = Ref(
            doi=doi_id,
            ref_type=parse_type(ref_data.get("type")),
            author=parse_authors(ref_data.get("author")),
            title=ref_data.get("title")[0],
            publisher=ref_data.get("publisher"),
            volume=ref_data.get("volume"),
            pages=ref_data.get("page"),
            url=ref_data.get("resource").get("primary").get("URL"),
            year=ref_data.get("published").get("date-parts")[0][0],
            month=ref_data.get("published").get("date-parts")[0][1],
            editor=parse_editors(ref_data.get("editor")),
            organization=parse_organization(ref_data.get("institution")),
            booktitle=next(iter(ref_data.get("container-title")), None),
            journal=next(iter(ref_data.get("container-title")), None)
            )
    print(new_ref)
    return new_ref


def parse_type(ref_type: str):
    if ref_type == "journal-article":
        return "article"
    if ref_type == "book":
        return "book"
    if ref_type == "proceedings-article":
        return "inproceedings"
    return "article"


def parse_authors(data: dict):
    if data is None:
        return None
    authors = []
    for author in data:
        authors.append(author.get("given") + " " + author.get("family"))
    return ", ".join(authors)


def parse_editors(data: list):
    if data is None:
        return None
    editors = []
    for editor in data:
        editors.append(editor.get("given") + " " + editor.get("family"))
    return ", ".join(editors)


def parse_organization(data):
    if data is None:
        return None
    org = data[0]
    return org.get("name")


def validate_doi(doi_id):
    suffix_chars = ascii_letters + "1234567890" + "-._;()/"
    try:
        prefix, suffix = doi_id.split("/", 1)
        if not prefix.startswith("10."):
            return False
        for part in prefix.split(".")[1:]:
            if not part.isnumeric():
                return False
        for c in suffix:
            if c not in suffix_chars:
                return False
        return True
    except Exception:
        return False
