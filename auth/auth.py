from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy


cookie_transport = CookieTransport(cookie_name="plants", cookie_max_age=3600)


SECRET = "SECRET" # этот ключ только для учебных целей, иначе он был бы длинным и был бы спрятан в .env и импортирован в config.py

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)