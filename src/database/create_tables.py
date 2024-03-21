from database.db_session import db
from services.notifications.models.notification import Notification

def create_tables(models):
    try:
        db.create_tables(models)
        db.close()
        print('Created Tables')
    except Exception as e:
        print(e)
        raise

def drop_tables(models):
    try:
        db.drop_tables(models)
        db.close()
        print("Dropped tables")
    except Exception as e:
        print(e)
        raise

# if __name__ == "__main__":
#     create_tables([Notification])