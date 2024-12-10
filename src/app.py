from flask import redirect, render_template, request, jsonify
from db_helper import reset_db
from config import app, test_env, db
from repositories.ref_repository import create_ref, get_refs
from repositories.ref_repository import delete_all_refs, delete_ref
from repositories.tag_repository import get_tags, link_many_tags_to_ref
from entities.ref import Ref


@app.route("/")
def index():
    tag_filter = request.args.get('tag_filter')
    refs = get_refs(db, tag_filter=tag_filter)
    bibtex = "\n\n".join(list(map(lambda ref: ref.get_bibtex(), refs)))
    return render_template("index.html", refs=refs, bibtex=bibtex)


@app.route("/add", methods=["GET", "POST"])
def route_add():
    if request.method == "GET":
        return render_template("add.html")

    fields = [
        "ref_type", "ref_name", "author", "title", "year", "publisher",
        "journal", "volume", "pages", "month", "doi", "note", "key", 
        "series", "address",  "edition", "url", "booktitle", "editor", 
        "organization"
    ]

    form_data = {}

    for field in fields:
        value = request.form.get(field)
        if field == "year" and value is not None:
            value = int(value)
        form_data[field] = value if value != "" else None

    new_ref = Ref(**{key: form_data.get(key) for key in fields})
    try:
        new_ref.validate()
        create_ref(db, new_ref)
    except Exception as e:
        return render_template("add.html", error_msg=str(e))

    return redirect("/")


@app.route("/<int:ref_id>/add_tags", methods=["GET", "POST"])
def add_tags(ref_id):
    if request.method == "GET":
        return render_template("add_tags.html",
                               tags=get_tags(db), ref_id=ref_id)
    if request.method == "POST":
        tag_names = request.form.getlist("tag_name")
        try:
            link_many_tags_to_ref(db, ref_id, tag_names)
        except Exception as e:
            return render_template("add_tags.html", error_msg=str(e),
                                   tags=get_tags(db), ref_id=ref_id)

    return redirect("/")


@app.route("/delete_all", methods=["POST"])
def delete_all():
    delete_all_refs(db)
    return redirect("/")


@app.route("/<int:ref_id>/delete_ref", methods=["POST"])
def delete_reference(ref_id):
    delete_ref(db, ref_id)
    return redirect("/")


if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
