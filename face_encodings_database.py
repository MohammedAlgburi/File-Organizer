import sys
import sqlite3 as sql
import numpy as np
import exceptions as ex

class FaceEncodingStorage:
    def __init__(self) -> None:
        self.conn = sql.connect("face_encoding.db")

    # TODO: finish this method
    def add_encodings(self, list_of_encodings: list):
        cursor = self.conn.cursor()
        for encoding in list_of_encodings:
            try: 
                self.conn.execute("INSERT INTO encodings (name, encoding) VALUES (?, ?)", (None, encoding.tobytes()))
            except sql.Error as e:
                raise ex.EncodingWriteError()
            
    def initialize_db(self) -> None:
        """Initializes the table used for storing image encodings."""
        try:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS encodings 
                            (name TEXT,
                            encoding BLOB PRIMARY KEY)""")
            self.conn.commit()

        except sql.Error:
            raise ex.EncodingDBInitError()


    def close(self) -> None:
        """Closes the connection to the database."""
        try:
            self.conn.close()
        except Exception as e:
            print("There was an error closing the database.")
            sys.exit(1)

