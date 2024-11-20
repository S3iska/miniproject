from flask import request, redirect
from entities.ref import Ref
from repositories.ref_repository import create_ref
from util import validate_ref, UserInputError


def add_ref(req: request):
    ref_type = req.form.get("type")
    ref_author = req.form.get("author")
    ref_title = req.form.get("title")
    ref_year = int(req.form.get("year"))
    ref_publisher = req.form.get("publisher")
    ref_name = req.form.get("refname")

    new_ref = Ref(None, ref_type, ref_name, ref_author, ref_title, ref_year, ref_publisher)

    try:
        validate_ref(new_ref)
        create_ref(new_ref)
    except Exception:
        return "Could not add reference"

    return redirect("/")
