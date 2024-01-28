from flask import Flask, request, jsonify

from models import db, User

app =Flask(__name__)
app.config['SECRET_KEY'] = 'bomahub-app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

db.init_app(app)

with app.app_context():
  db.create_all()
  

@app.route("/")
def welcome():
  return "<p>Welcome to this api</p>"

@app.route("/signup", methods=["POST"])
def signup():
  email = request.json["email"]
  password = request.json["password"]
  
  user_exists = User.query.filter(email=email).first() is not None
  
  if user_exists:
    return jsonify({"error":"Email already exists"}),400
  
  return jsonify({
    "id":"1",
    "email":email
  })
  
if __name__ == "main":
  app.run(debug=True)