from sqlalchemy import (
    MetaData, String, Table, DECIMAL, Integer, Column
)


metadata = MetaData()


postcode = Table(
    'postcodes',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('code', String(), default=''),
    Column('latitude', DECIMAL(8, 6), nullable=False),
    Column('longitude', DECIMAL(9, 6), nullable=False),
)
