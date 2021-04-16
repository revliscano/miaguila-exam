from sqlalchemy import select, func
from .setup import data_access_layer


class Repository:
    def __init__(self, data_access_layer=data_access_layer):
        self.database = data_access_layer

    def copy_content_of(self, file):
        raw_connection = self.database.raw_connection
        cursor = raw_connection.cursor()
        command = (
            'COPY postcodes(latitude, longitude) '
            'FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        )
        cursor.copy_expert(command, file)
        raw_connection.commit()

    def __len__(self):
        count = select((func.count(),)).select_from(
            self.database.postcode
        )
        result = self.database.connection.execute(count)
        count, = result.fetchone()
        return count
