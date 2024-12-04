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


def link_tag_to_ref(db, ref_id, tag_name):
    checkquery = text("SELECT tag_id, tag_name FROM tags \
            WHERE tag_name = :tag_name")
    result = db.session.execute(checkquery, {"tag_name": tag_name}).fetchone()
    if result.tag_name != tag_name:
        new_tag = Tag(tag_name=tag_name)
        validate_tag(new_tag)
        create_tag(db, new_tag)
        link_tag = new_tag
    else:
        link_tag = Tag(result.tag_id, result.tag_name)
    try:
        sql = text("INSERT INTO ref_tags (ref_id, tag_id) \
                VALUES (:ref_id, :tag_id)")
        db.session.execute(sql, {"ref_id": ref_id, "tag_id": link_tag.tag_id})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def link_many_tags_to_ref(db, ref_id, tag_names):
    for tag_name in tag_names:
        link_tag_to_ref(db, ref_id, tag_name)
