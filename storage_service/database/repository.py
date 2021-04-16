from sqlalchemy import select, func
from .setup import data_access_layer


class Repository:
    def copy_content_of(self, file):
        raw_connection = data_access_layer.raw_connection
        cursor = raw_connection.cursor()
        command = (
            'COPY postcodes(latitude, longitude) '
            'FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        )
        cursor.copy_expert(command, file)
        raw_connection.commit()

    def __len__(self):
        count_command = select((func.count(),)).select_from(
            data_access_layer.postcode
        )
        result = data_access_layer.connection.execute(count_command)
        count, = result.fetchone()
        return count
