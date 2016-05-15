from project.settings.defaults import *  # NOQA


import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES["default"] = dj_database_url.config()
