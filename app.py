from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"#"postgresql://postgres:Tavishi%2A1234@db.gbxgrkpwoqllqziwvqtv.supabase.co:5432/postgres"#  # Use PostgreSQL/MySQL in production
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Serve the frontend page
@app.route("/")
def index():
    return render_template("index.html")

# Signup API
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name, email, password = data.get("name"), data.get("email"), data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    # print(password) # Tavishi
    new_user = User(name=name, email=email, password=hashed_password.decode("utf-8"))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
