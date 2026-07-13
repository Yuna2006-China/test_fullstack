from flask import Flask, jsonify
from flask_cors import CORS
from config.settings import DB_URL
from models.database import db
# from api import all_bps

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# for bp, prefix in all_bps:
#     app.register_blueprint(bp, url_prefix=prefix)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "msg": "Flask backend running success",
        "db_url": DB_URL.split("@")[0] + "@***"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
