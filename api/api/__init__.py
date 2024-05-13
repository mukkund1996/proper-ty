import pathlib
import connexion
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_caching import Cache

API_PORT = os.environ.get("API_PORT", 8000)
basedir = pathlib.Path(__file__).parent.resolve()
SEED_DATA_PATH = os.environ.get("SEED_DATA_PATH", basedir.parent.parent / "seed" / "Enodo_Skills_Assessment_Data_File.xlsx")

ma = Marshmallow()
db = SQLAlchemy()
cache = Cache()

def create_app():
    connex_app = connexion.App("PROPER-ty-api", specification_dir=basedir)
    connex_app.add_api(basedir / 'spec' / "swagger.yml")

    app = connex_app.app

    db_path = os.environ.get("SQLITE_PATH", basedir.parent.parent / "db" / "properties.db")

    config = {
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "CORS_HEADERS": "Content-Type",
    }

    CORS(app)
    app.config.from_mapping(config)

    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)

    return app