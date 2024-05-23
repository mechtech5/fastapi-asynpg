import os
import re


def error_loc(loc: list):
    """
    This function is used to return an error message when there
    is a validation exception.

    :param loc:list: Determine the location of the error
    :return: The location of the error
    """
    tokens = []
    for i in range(0, len(loc)):
        if str(loc[i]).isdigit():
            index = len(tokens) - 1
            tokens[index] = tokens[index] + "[" + str(loc[i]) + "]"
        else:
            tokens.append(loc[i])
    return ".".join(tokens)


def check_password(password: str):
    # Check if the password length is between 8 and 15 characters
    if 8 <= len(password) <= 20:
        # Check if the password contains at least one upper case letter
        if any(char.isupper() for char in password):
            # Check if the password contains at least one special character
            if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                # Check if the password contains at least one number
                if any(char.isdigit() for char in password):
                    return True
    return False


def is_valid_password(password: str):
    if not check_password(password):
        raise ValueError("please give strong password with min 8 to max 15 char")
    else:
        return password


def get_frontend_url():
    env = os.getenv("BACKEND_ENV", "local")

    if env == "dev":
        url = "https://dev.trustool.nl/2fa"
    elif env == "prod":
        url = "https://app.trustool.nl/2fa"
    else:
        url = "http://localhost:3000/2fa"

    return url


def get_url():
    env = os.getenv("BACKEND_ENV", "local")

    if env == "dev":
        url = "https://dev.trustool.nl/login"
    elif env == "prod":
        url = "https://app.trustool.nl/login"
    else:
        url = "http://localhost:3000/login"

    return url
