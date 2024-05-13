from distutils.core import setup

setup(
    name='api',
    version='1.0',
    packages=['api',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('../README.md').read(),
    install_requires=["Flask-SQLAlchemy", "Flask-Migrate", "SQLAlchemy", "connexion[swagger-ui]", "flask-marshmallow[sqlalchemy]", "flask-cors", "Flask-Caching"],
    extras_require={"seed": ["pandas"], "test": ["pytest", "pytest-flask"]},
)