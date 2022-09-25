from utils.cfg import cfg

DEBUG = cfg("debug", is_bool=True)

# DATABASES
DATABASES = {
    "default": {
        "ENGINE": cfg("db", "engine"),
        "NAME": cfg("db", "name"),
        "USER": cfg("db", "user"),
        "PASSWORD": cfg("db", "pswd"),
        "HOST": cfg("db", "host"),
        "POST": cfg("db", "port", is_int=True),
    },
    "mongo": {
        "ENGINE": "djongo",
        "ENFORCE_SCHEMA": True,
        "NAME": cfg("mongo", "name"),
        "CLIENT": {
            "host": cfg("mongo", "host"),
            "port": cfg("mongo", "port", is_int=True),
            "username": cfg("mongo", "user"),
            "password": cfg("mongo", "pswd"),
        },
    },
}
DATABASE_APPS_MAPPING = {
    "study": "mongo",
}
DATABASE_ROUTERS = ["dessert_campus.database_router.DatabaseAppsRouter"]

# COS
COS_URL = cfg("cos", "url")
COS_SECRETID = cfg("cos", "secretid")
COS_SECRETKEY = cfg("cos", "secretkey")
COS_REGION = cfg("cos", "region")
COS_SCHEME = cfg("cos", "scheme")
COS_BUCKET = cfg("cos", "bucket")
COS_ALLOWED_EXT = cfg("cos", "allowed_ext", is_eval=True)

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = cfg("email", "host")
EMAIL_PORT = cfg("email", "port", is_int=True)
EMAIL_HOST_USER = cfg("email", "user")
EMAIL_HOST_PASSWORD = cfg("email", "pswd")
EMAIL_FROM = cfg("email", "from")
EMAIL_USE_SSL = cfg("email", "ssl", is_bool=True)

# WECHAT
WECHAT_APPID = cfg("wechat", "appid")
WECHAT_APPSECRET = cfg("wechat", "appsecret")
