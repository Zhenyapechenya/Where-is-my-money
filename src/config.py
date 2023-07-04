from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

SECRET_AUTH = os.environ.get("SECRET_AUTH")

SMTP_HOST = 'smtp.yandex.ru'
SMTP_PORT = 465
SMTP_USERNAME = 'your_username'
SMTP_PASSWORD = 'g5e-YG2-dpi-56d'
SENDER_EMAIL = 'shift.test@yandex.ru'
