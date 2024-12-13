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

def validate_int(value, name, optional, min_value, max_value):
    if value is None and not optional:
        raise UserInputError(f"{name} is requried.")

    if not min_value <= value <= max_value:
        raise UserInputError(
            f"{name} must be between {min_value} and {max_value}"
        )
