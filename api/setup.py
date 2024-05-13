from distutils.core import setup

setup(
    name='api',
    description='REST API for Properties Database',
    version='1.0',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=["Flask-SQLAlchemy", "Flask-Migrate", "SQLAlchemy", "connexion[swagger-ui]", "flask-marshmallow[sqlalchemy]", "flask-cors", "Flask-Caching"],
    extras_require={"seed": ["pandas", "openpyxl"], "test": ["pytest", "pytest-flask"]},
)