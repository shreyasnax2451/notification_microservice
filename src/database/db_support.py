from database.db_session import db
from fastapi import Depends
import time

def get_db():
    try:
        db.connect(reuse_if_open=True)
        yield db
    finally:
        if not db.is_closed():
            db.close()