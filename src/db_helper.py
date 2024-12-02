from sqlalchemy import text
from config import db, app

def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def delete_table_if_exists(name):
    if table_exists(name):
        sql = text(f"DROP TABLE {name} CASCADE;")
        db.session.execute(sql)
        db.session.commit()

def setup_db():
    delete_table_if_exists("refs")
    delete_table_if_exists("tags")
    delete_table_if_exists("ref_tags")

    sql = text("SELECT 1;")
    with open('schema.sql', 'r', encoding="utf-8") as file:
        sql = text(file.read())

    db.session.execute(sql)
    test_data_sql = text("SELECT 1;")
    with open('test_data.sql', 'r', encoding="utf-8") as file:
        test_data_sql = text(file.read())

    db.session.execute(test_data_sql)
    db.session.commit()

def reset_db():
    setup_db()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
