from dataclasses import fields
from sqlalchemy import text
from entities.ref import Ref

def ref_from_row(row):
    ref_data = {
        field.name: getattr(row, field.name, None) for field in fields(Ref)
    }
    ref = Ref(**ref_data)
    ref.tags = row.tags
    return ref

def get_refs(db, **kwargs):
    valid_fields = [field.name for field in fields(Ref)]
    query_fields = ", ".join([f"r.{field}" for field in valid_fields])

    query = f"""
        SELECT 
            {query_fields},
            array_remove(array_agg(t.tag_name), NULL) as tags
        FROM refs r
            LEFT JOIN ref_tags rt ON r.id = rt.ref_id
            LEFT JOIN tags t      ON rt.tag_id = t.tag_id
    """

    conditions = []
    params = {}
    for field in valid_fields:
        if field in kwargs and kwargs[field] is not None:
            conditions.append(f"r.{field} = :{field}")
            params[field] = kwargs[field]
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " GROUP BY r.id"

    result = db.session.execute(text(query), params)
    rows = result.fetchall()
    return [ref_from_row(row) for row in rows]


def create_ref(db, ref: Ref):
    fields_to_insert = [
        field.name for field in fields(Ref)
        if getattr(ref, field.name) is not None]
    columns = ", ".join(fields_to_insert)
    placeholders = ", ".join([f":{field}" for field in fields_to_insert])

    sql = text(f"""
        INSERT INTO refs ({columns})
        VALUES ({placeholders})
    """)
    db.session.execute(sql, {
        field: getattr(ref, field) for field in fields_to_insert})
    db.session.commit()


def delete_ref(db, ref_id):
    sql = text("DELETE FROM refs WHERE id = :id")
    db.session.execute(sql, {"id": ref_id})
    db.session.commit()


def delete_all_refs(db):
    sql = text("TRUNCATE refs, ref_tags")
    db.session.execute(sql)
    db.session.commit()
