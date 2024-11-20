from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
from util import validate_ref
from repositories.ref_repository import create_ref
from entities.ref import Ref


@app.route("/")
def index():
    return "Test"


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})


@app.route("/add", methods=["GET", "POST"])
def route_add():
    if request.method == "GET":
        return render_template("add.html")
    ref_type = request.form.get("type")
    ref_author = request.form.get("author")
    ref_title = request.form.get("title")
    ref_year = int(request.form.get("year"))
    ref_publisher = request.form.get("publisher")
    ref_name = request.form.get("refname")

    new_ref = Ref(None, ref_type, ref_name, ref_author, ref_title, ref_year, ref_publisher)

    try:
        validate_ref(new_ref)
        create_ref(new_ref)
    except Exception:
        return "Could not add reference"

    return redirect("/")
