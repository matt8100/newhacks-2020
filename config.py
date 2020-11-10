import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRETKEY") or "SECRETKEY2"