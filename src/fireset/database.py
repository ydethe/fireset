import psycopg

from . import settings


def list_vcards():
    # Connect to an existing database
    with psycopg.connect(settings.database_uri.unicode_string()) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM organisation")
            cur.fetchone()
