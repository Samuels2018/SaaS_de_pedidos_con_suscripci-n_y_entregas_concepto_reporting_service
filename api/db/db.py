import os
from pymongo import MongoClient
from pymongo.database import Database
from typing import Any

def set_db () -> Database[Any]:
  """ connection to the database """
  # MongoDB connection string
  mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
  client: MongoClient = MongoClient(
    mongo_uri,
    tls=True,  # Para conexiones seguras
    retryWrites=True,
    w="majority",
    appname="ReportingService",
    connectTimeoutMS=5000,
    socketTimeoutMS=30000
  )
    
  # Verificar conexión
  try:
    client.admin.command('ping')
    print("Conexión exitosa a MongoDB")
  except Exception as err:
    print(f"Error de conexión a MongoDB: {err}")
    raise

  db = client["reporting_db"]
  
  return db