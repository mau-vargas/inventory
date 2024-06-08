from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# DATABASE_URL = os.getenv("DATABASE_URL")

# Docker
# DATABASE_URL = 'postgresql://admin_user:admin_password@posgres:5432/inventory_db'

# Local
DATABASE_URL = 'postgresql://admin_user:admin_password@localhost:5432/inventory_db'


# Kubernetes
# DATABASE_URL = 'postgresql://admin_user:admin_password@postgres-service:5432/inventory_db'


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
