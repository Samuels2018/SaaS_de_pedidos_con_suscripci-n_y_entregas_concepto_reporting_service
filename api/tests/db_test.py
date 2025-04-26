import pytest
from api.db import set_db
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

def test_db_connection_seccess (app) -> None:
  """Test successful connection to the database."""

  with app.app_context():
    db = set_db()
    assert db is not None
    assert db.command('ping') == {'ok': 1.0}

def test_db_connection_failure (monkeypatch) -> None:
  monkeypatch.setenv("MONGO_URI", "mongodb://invalid_uri:27017/")

  with pytest.raises((ConnectionFailure, ServerSelectionTimeoutError)):
    set_db()

def test_db_connection_timeout (monkeypatch) -> None:
  monkeypatch.setenv("MONGO_URI", "mongodb://localhost:27017/")
  monkeypatch.setenv("MONGO_TIMEOUT", "0")  # Set a very low timeout

  with pytest.raises((ConnectionFailure, ServerSelectionTimeoutError)):
    set_db()

def test_db_collections (app) -> None:
  with app.app_context():
    db = set_db()
    collections = db.list_collection_names()
    assert "usage_metrics" in collections
    assert "subscriptions" in collections
