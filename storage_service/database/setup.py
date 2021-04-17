from sqlalchemy import (
    MetaData, String, Table, DECIMAL, Integer, Column, create_engine
)


DATABASE_URL = 'postgresql://miaguila:miaguila@localhost/storage_service_db'


class DataAccessLayer:
    engine = None
    conn_string = None
    metadata = MetaData()
    connection = None

    locations = Table(
        'locations',
        metadata,
        Column('id', Integer(), primary_key=True),
        Column('postcode', String(), default=''),
        Column('latitude', DECIMAL(8, 6), nullable=False),
        Column('longitude', DECIMAL(9, 6), nullable=False),
    )

    def db_init(self, conn_string=DATABASE_URL):
        self.engine = create_engine(conn_string or self.conn_string)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

    def close_connection(self):
        self.connection.close()

    @property
    def raw_connection(self):
        return self.engine.raw_connection()


data_access_layer = DataAccessLayer()
