import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
cors = CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'properties.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CORS_HEADERS"] = "Content-Type"

db = SQLAlchemy(app)
ma = Marshmallow(app)