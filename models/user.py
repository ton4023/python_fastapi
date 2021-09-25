from sqlalchemy import Table,Column
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

users= Table(
    'users',meta,
    Column('id', Integer,primary_key=true),
    Column('username', String(255)),
    Column('email', String(255)),
    Column('password', String(255)),
)