from flask import render_template
import config

API_PORT = 8000

app = config.connex_app
app.add_api(config.basedir.parent / 'spec' / "swagger.yml")

@app.route("/")
@config.cache.cached(timeout=50)
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=API_PORT, debug=True)