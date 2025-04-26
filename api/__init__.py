from flask import Flask
from api import db
from api.services import init_services

def create_app() -> Flask:
  """Create and configure the Flask application."""
  app = Flask(__name__)
  db.set_db()
  init_services(app)
  return app

