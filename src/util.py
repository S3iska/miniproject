class UserInputError(Exception):
    pass

def validate_string(value, name, optional, min_length, max_length):
    if value is None or value == "":
        if not optional:
            raise UserInputError(f"{name} is required.")
        return

    if not min_length <= len(value) <= max_length:
        raise UserInputError(
            f"{name} must be between {min_length} and {max_length}"
            " characters long."
        )
