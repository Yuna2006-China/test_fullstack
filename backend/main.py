from flask import Flask, jsonify
from flask_cors import CORS
from config.settings import DB_URL
from db.database import db

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

from db.models import User, Product
from api.user_product import up_bp
app.register_blueprint(up_bp, url_prefix="/api")

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "msg": "Flask backend running success",
        "db_url": DB_URL.split("@")[0] + "@***"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
