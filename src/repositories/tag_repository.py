from sqlalchemy import text
from entities.tag import Tag, validate_tag


class DBError(Exception):
    pass


def create_tag(db, tag: Tag):
    try:
        query = text("INSERT INTO tags (tag_name) VALUES (:name)")
        db.session.execute(query, {"name": tag.tag_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def get_tags(db):
    query = text("""
                 SELECT tag_id, tag_name
                 FROM tags
                 """)
    result = db.session.execute(query)
    tags = []
    for row in result:
        new_tag = Tag(tag_id=row.tag_id, tag_name=row.tag_name)
        validate_tag(new_tag)
        tags.append(new_tag)
    return tags

def get_tags_by_ref(db, ref_id):
    query = text("""
                 SELECT t.tag_id, tag_name
                 FROM ref_tags rt
                 LEFT JOIN tags t ON rt.tag_id=t.tag_id WHERE rt.ref_id = :ref_id
                 """)
    result = db.session.execute(query, {"ref_id": ref_id}).fetchall()
    tags = []
    for row in result:
        ref_tags = Tag(tag_id=row.tag_id, tag_name=row.tag_name)
        tags.append(ref_tags)
    return tags

def link_tag_to_ref(db, ref_id, tag_name):
    checkquery = text("SELECT tag_id, tag_name FROM tags \
            WHERE tag_name = :tag_name")
    result = db.session.execute(checkquery, {"tag_name": tag_name}).fetchone()
    if not result:
        tag = Tag(tag_name=tag_name)
        validate_tag(tag)
        create_tag(db, tag)
    else:
        tag = Tag(result.tag_id, result.tag_name)
    try:
        sql = text("INSERT INTO ref_tags (ref_id, tag_id) \
                SELECT :ref_id, tag_id \
                FROM tags \
                WHERE tag_name = :tag_name")
        db.session.execute(sql, {"ref_id": ref_id, "tag_name": tag_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def link_many_tags_to_ref(db, ref_id, tag_names):
    for tag_name in tag_names:
        link_tag_to_ref(db, ref_id, tag_name)
