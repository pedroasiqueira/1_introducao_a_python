def validate_email(email):
    index = 0
    # validar primeira letra
    if not email[index].isalpha():
        raise ValueError("Username should starts with a letter")

    # validar username
    while email[index] != "@" and index < len(email):
        letter = email[index]
        if not letter.isalpha() and not letter.isdigit() and letter not in ("_", "-"):
            raise ValueError(
                "Username should contains only letters, "
                "digits, dashes or underscores"
            )
        index += 1
    index += 1

    # validar website

    # validar extensão

    return None
