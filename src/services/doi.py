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
            editor=parse_editor(ref_data.get("editor")),
            organization=parse_organization(ref_data.get("institution")),
            )
    print(new_ref)
    return new_ref


def parse_type(ref_type: str):
    if ref_type == "journal-article":
        return "article"
    elif ref_type == "book":
        return "book"
    return "article"


def parse_authors(data: dict):
    authors = []
    for author in data:
        authors.append(author.get("given") + " " + author.get("family"))
    return ", ".join(authors)


def parse_editor(data: list):
    if data is None:
        return None
    return data[0].get("given") + " " + data[0].get("family")


def parse_organization(data):
    if data is None:
        return None
    org = data[0]
    return org.get("name")


def get_url_for_doi(doi_id):
    if not validate_doi(doi_id):
        return None
    response = get(f"https://doi.org/api/handles/{doi_id}", timeout=2)
    if response.status_code != 200:
        return None
    data = response.json().get("values")[0]
    if data.get("type") != "URL":
        return None
    data = data.get("data")
    if data.get("format") == "string":
        return data.get("value")
    return None


def validate_doi(doi_id):
    try:
        prefix, suffix = doi_id.split("/", 1)
        if not prefix.startswith("10."):
            return False
        for part in prefix.split(".")[1:]:
            if not part.isnumeric():
                return False
        for part in suffix.split("."):
            if not part.isalnum():
                return False
        return True
    except Exception:
        return False
