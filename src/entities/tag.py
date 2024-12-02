from dataclasses import dataclass


class UserInputError(Exception):
    pass


@dataclass
class Tag:
    tag_id: int = None
    tag_name: str = None


def validate_tag(tag: Tag):
    if not tag.tag_name:
        raise UserInputError("Tag must have a name.")
    if len(tag.tag_name) <= 2:
        raise UserInputError("Tag must be atleast three characters long.")
    if not tag.tag_name.isalnum():
        raise UserInputError("Tag can only contain letters and numbers.")

    if not tag.tag_id:
        raise UserInputError("Tag does not have an id.")
