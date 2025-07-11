import sqlite3 as sql
import numpy as np
from exceptions import CloseDataBaseError, EncodingDBInitError, EncodingWriteError

class FaceEncodingStorage:
    def __init__(self) -> None:
        self.conn = sql.connect("face_encoding.db")
        if self.check_table_exist() == False:
            self.initialize_db()

    def add_encodings(self, encodings: list[np.ndarray]) -> None:
        """Adds a list of encodings into the database
        
            Args:
                list_of_encodings (list): list of encodings which will be added to the database.

            Raises: 
                EncodingWriteError: if there was an error from sqlite3 module.
        """
        for encoding in encodings:
            if self.check_encoding(encoding):
                continue
            try: 
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO encodings (name, encoding) VALUES (?, ?)", (None, encoding.tobytes()))
                self.conn.commit()
                cursor.close()
            except sql.Error:
                raise EncodingWriteError()
        
    def initialize_db(self) -> None:
        """Initializes the table used for storing image encodings.
        
            Raises:
                EncodingDBInitError: if there was an sqlite3 error when initializing the database.
        """
        try:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS encodings 
                            (name TEXT,
                            encoding BLOB PRIMARY KEY)""")
            self.conn.commit()

        except sql.Error:
            raise EncodingDBInitError()


    def close(self) -> None:
        """Closes the connection to the database.

            Raises:
                CloseDataBaseError: if there was an sqlite3 error when closing the database.    
        
        """
        try:
            self.conn.close()
        except sql.Error:
            raise CloseDataBaseError()

    def check_table_exist(self) -> bool:
        """Checks if db exists.
        
            Returns:
                bool: True if database exists.
        
        """
        cursor = self.conn.cursor()
        db = cursor.execute("SELECT name FROM sqlite_master WHERE name = 'encodings'")
        if db.fetchone() is None:
            return False
        return True

    def check_encoding(self, encoding: np.ndarray) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT encoding FROM encodings WHERE encoding = ?", encoding.tobytes())
        result = cursor.fetchone()
        if result:
            return True
        return False
