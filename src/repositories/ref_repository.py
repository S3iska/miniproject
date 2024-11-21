from sqlalchemy import text
from config import db
from entities.ref import Ref


def ref_from_row(row):
    return Ref(
        id = row.id,
        ref_type = row.type,
        ref_name = row.ref_name,
        author = row.author,
        title = row.title,
        year = row.year,
        publisher = row.publisher
    )


def get_refs():
    result = db.session.execute(text("""
        SELECT id, type, ref_name, author, title, year, publisher
        FROM refs
    """))
    refs = result.fetchall()

    return [ref_from_row(ref) for ref in refs]


def get_selected_refs(**kwargs):
    """
    Fetches rows from the 'refs' table based on provided filter criteria. If no
    filters are specified, all rows are retrieved. Filters can be passed as
    named arguments (e.g., id=1, type='book'). The results are returned as
    a list of Ref objects, constructed dynamically by unpacking database rows.
    """

    query = """
        SELECT id, type, ref_name, author, title, year, publisher
        FROM refs
    """

    valid_fields = [
        'id', 'type', 'ref_name', 'author', 'title', 'year', 'publisher'
    ]

    conditions = []
    params = {}

    for field in valid_fields:
        if field in kwargs and kwargs[field] is not None:
            conditions.append(f"{field} = :{field}")
            params[field] = kwargs[field]

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    result = db.session.execute(text(query), params)
    refs = result.fetchall()

    return [ref_from_row(ref) for ref in refs]


def create_ref(ref: Ref):
    sql = text("""
        INSERT INTO refs (type, ref_name, author, title, year, publisher)
        VALUES (:type, :ref_name, :author, :title, :year, :publisher)
    """)
    db.session.execute(sql, {
        "type": ref.ref_type,
        "ref_name": ref.ref_name,
        "author": ref.author,
        "title": ref.title,
        "year": ref.year,
        "publisher": ref.publisher
    })
    db.session.commit()
