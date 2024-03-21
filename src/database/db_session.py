from peewee import PostgresqlDatabase
from configs.env import *
import logging
from contextvars import ContextVar

db = PostgresqlDatabase(
    DATABASE_NAME,
    autorollback=True,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD
)