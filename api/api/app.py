from flask import render_template
import config

config.connex_app.add_api(config.basedir.parent / 'spec' / "swagger.yml")

@config.connex_app.route("/")
@config.cache.cached(timeout=50)
def home():
    return render_template("home.html")

if __name__ == "__main__":
    config.connex_app.run(host="0.0.0.0", port=config.API_PORT, debug=True)