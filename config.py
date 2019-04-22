import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRCK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://jeremywells:password@localhost/jeremywells"
SQLALCHEMY_DATABASE_URI = "postgresql://localhost"
