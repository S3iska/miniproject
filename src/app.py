from flask import redirect, render_template, request, jsonify
from db_helper import reset_db
from config import app, test_env, db
from util import validate_ref
from repositories.ref_repository import create_ref, get_refs
from repositories.ref_repository import delete_all_refs, delete_ref
from entities.ref import Ref


@app.route("/")
def index():
    refs = get_refs(db)
    bibtex = "\n\n".join(list(map(lambda ref: ref.get_bibtex(), refs)))
    return render_template("index.html", refs=get_refs(db), bibtex=bibtex)


@app.route("/add", methods=["GET", "POST"])
def route_add():
    if request.method == "GET":
        return render_template("add.html")

    ref_type = request.form.get("type")
    ref_name = request.form.get("refname")
    ref_author = request.form.get("author")
    ref_title = request.form.get("title")
    ref_year = int(request.form.get("year"))
    ref_publisher = request.form.get("publisher")

    new_ref = Ref(
        ref_type = ref_type,
        ref_name = ref_name,
        author = ref_author,
        title = ref_title,
        year = ref_year,
        publisher = ref_publisher
    )

    try:
        validate_ref(new_ref)
        create_ref(db, new_ref)
    except Exception as e:
        return render_template("add.html", error_msg=str(e))

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
