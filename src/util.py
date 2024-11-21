from entities.ref import Ref

class UserInputError(Exception):
    pass

def validate_article_ref(ref: Ref):
    if not ref.author:
        raise UserInputError("Author field is required.")
    if not 3 <= len(ref.author) <= 100:
        raise UserInputError(
            "Author name must be between 3 and 100 characters long"
        )

    if not ref.title:
        raise UserInputError("Title field is required.")
    if not 3 <= len(ref.title) <= 250:
        raise UserInputError(
            "Title must be between 3 and 250 characters long"
        )

    if not ref.year:
        raise UserInputError("Year field is required.")
    if not 1600 < ref.year < 2100:
        raise UserInputError("Year must be between 1600 and 2100")

def validate_ref(ref: Ref):
    if not ref.ref_type:
        raise UserInputError("Reference type is required.")

    if not ref.ref_name:
        raise UserInputError("Reference name is required.")
    if not len(ref.ref_name) <= 100:
        raise UserInputError(
            "Reference name must be less than 100 characters long."
        )

    if ref.ref_type == "article":
        validate_article_ref(ref)
    else:
        raise UserInputError("Invalid reference type.")
