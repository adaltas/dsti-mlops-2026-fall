import re


def app():
    u_name = get_user_name_from_input()

    if not u_name:
        print("No valid user created, exiting")
    else:
        get_email_from_input()
        get_display_name_from_input(u_name)


def get_email_from_input() -> str | None:
    """Use regex pattern to validate user email obtained from input.
    Rules:
        - must begin with a letter
        - after alphanumeric chars and '.' are allowed.
        - '..' is not allowed
        - only one '@' allowed
        - a '.' must exist after the '@'
    """

    pattern = r"^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
    email = input("Tell me your email: ")

    if not re.match(pattern, email):
        print("Email is not valid.")
    else:
        return email


def get_user_name_from_input() -> str | None:
    """Not empty string. No spaces."""
    username = input("Create your user name: ")
    if not username or " " in username:
        message="Username is not valid"
        print(message)
        return None
    else:
        return username


def get_display_name_from_input(
    u_name: str,
    banned_names: list[str] | None = None
) -> str | None:
    """Prompt for a display name/handle.

    Rules:
        - Defaults to u_name if empty
        - Must be 3-20 characters long
        - Must begin with a letter and only contain alphanumeric chars and/or
          underscore
        - Cannot be in optionally provided banned_names (case-insensitive)
    """

    if banned_names is None:
        banned_names = []

    d_name = input("Create your display name/handle: ")

    if not d_name:
        print(f"Display name not entered. Defaulting to username: {u_name}")
        return u_name
    elif len(d_name) < 3 or len(d_name) > 20:
        message = "Display Name should be between 3 and 20 characters"
        print(message)
        return None
    elif not re.search(r"^[a-zA-Z][a-zA-Z0-9_]*$", d_name):
        message = (
        "Display name must start with a letter and contain only letters, "
        "numbers, or underscores."
        )
        print(message)
        return None
    elif d_name.lower() in [name.lower() for name in banned_names]:
        print("Invalid display name.")
        return None
    else:
        return d_name


if __name__ == "__main__":
    app()

# TODO: Seperate I/O from validation logic
