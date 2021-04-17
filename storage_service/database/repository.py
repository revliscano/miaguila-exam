from sqlalchemy import select, func
from sqlalchemy.sql.expression import bindparam
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

    def fetch_locations_without_postcodes(self):
        postcode_field = self.table.c.postcode
        result = data_access_layer.connection.execute(
            self.table
            .select()
            .where(func.coalesce(postcode_field, '') == '')
            .limit(100)
        ).fetchall()
        return result

    def update(self, locations):
        latitude_field = self.table.c.latitude
        longitude_field = self.table.c.longitude
        data_access_layer.connection.execute(
            self.table
            .update()
            .where(
                latitude_field == bindparam('_latitude')
                and longitude_field == bindparam('_longitude')
            )
            .values(
                {'postcode': bindparam('postcode')}
            ),
            locations
        )

    def __len__(self):
        count_command = select((func.count(),)).select_from(
            self.table
        )
        result = data_access_layer.connection.execute(count_command)
        count, = result.fetchone()
        return count
