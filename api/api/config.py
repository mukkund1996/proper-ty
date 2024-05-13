import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_caching import Cache

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app

config = {
    "SQLALCHEMY_DATABASE_URI": f"sqlite:///{basedir / 'properties.db'}",
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "CORS_HEADERS": "Content-Type",
}

cors = CORS(app)
app.config.from_mapping(config)

cache = Cache(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)