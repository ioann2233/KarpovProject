from service.testing.user import get_user_by_username


def authenticate_user(username: str, password: str):
    user = get_user_by_username(username.strip())
    if not user or user.password != password:
        return None
    return user
