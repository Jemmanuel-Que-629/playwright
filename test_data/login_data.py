VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


INVALID_LOGIN_SCENARIOS = [
    ("standard_user", "wrong_password"),
    ("wrong_user", "secret_sauce"),
    ("", "secret_sauce"),
    ("standard_user", ""),
]