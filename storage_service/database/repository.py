from sqlalchemy import select, func
from database.setup import data_access_layer


class Repository:

    table = data_access_layer.locations

    def copy_content_of(self, file):
        raw_connection = data_access_layer.raw_connection
        cursor = raw_connection.cursor()
        command = (
            'COPY locations(latitude, longitude) '
            'FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        )
        cursor.copy_expert(command, file)
        raw_connection.commit()

    def fetch_batch_with_null_postcode(self):
        code_field = self.table.c.code
        result = data_access_layer.connection.execute(
            self.table
            .select()
            .where(func.coalesce(code_field, '') == '')
            .limit(100)
        ).fetchall()
        return result

    def __len__(self):
        count_command = select((func.count(),)).select_from(
            self.table
        )
        result = data_access_layer.connection.execute(count_command)
        count, = result.fetchone()
        return count
