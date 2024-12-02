from sqlalchemy import text
from entities.tag import Tag


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
        tags.append(Tag(tag_id=row.tag_id, tag_name=row.tag_name))
    return tags
