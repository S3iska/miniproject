from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
from add import add_ref


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
    try:
        add_ref(request)
    except Exception as e:
        raise e

    return redirect("/")
