from flask import Flask, render_template,send_from_directory
from database import db
import os
from models import Dataset
from routes.datasets import datasets_bp
from routes.reports import reports_bp
from routes.auth import auth_bp

app = Flask(
    __name__
)
app.secret_key = "data-quality-secret-key"

# Database Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(BASE_DIR, "data_quality.db")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db.init_app(app)
app.register_blueprint(datasets_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/dataset/<int:dataset_id>")
def dataset_details(dataset_id):
    return render_template(
        "dataset-details.html",
        dataset_id=dataset_id
    )


# Create database tables (currently none)
with app.app_context():
    db.create_all()
    from models import User

    if not User.query.filter_by(username="admin").first():
        user = User(username="admin")
        user.set_password("admin123")

        db.session.add(user)
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)


