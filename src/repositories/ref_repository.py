from config import db
from sqlalchemy import text

from entities.Ref import Ref


def get_refs():
    result = db.session.execute(text("""
        SELECT id, type, ref_name, author, title, year, publisher
        FROM refs
    """))
    refs = result.fetchall()
    return [Ref(ref[0], ref[1], ref[2], ref[3], ref[4], ref[5], ref[6]) for ref in refs] 


def create_ref(ref: Ref):
    sql = text("""
        INSERT INTO todos (id, type, ref_name, author, title, year, publisher)
        VALUES (:id, :type, :ref_name, :author, :title, :year, :publisher)
    """)
    db.session.execute(sql, {
        "id": ref.id,
        "type": ref.type,
        "ref_name": ref.ref_name,
        "author": ref.author,
        "title": ref.title,
        "year": ref.year,
        "publisher": ref.publisher
    })
    db.session.commit()
