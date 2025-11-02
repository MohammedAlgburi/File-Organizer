import sqlite3 as sql
import numpy as np
from exceptions import CloseDBError, EmbeddingDBInitError, EmbeddingWriteError, ChangeEmbeddingNameError

class FaceEmbeddingStorage:
    def __init__(self) -> None:
        self.conn = sql.connect("face_embeddings.db")

        if self.check_table_exist() == False:
            self.initialize_db()

    def add_embeddings(self, embeddings: list[np.ndarray]) -> None:
        """Adds a list of embeddings into the database
        
            Args:
                embeddings (list): list of embedding which will be added to the database.

            Raises: 
                EmbeddingWriteError: if there was an error from sqlite3 module.
        """
        for embedding in embeddings:
            if self.check_embedding(embedding):
                continue
            try: 
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO embeddings (name, embedding) VALUES (?, ?)", (None, embedding.tobytes()))
                self.conn.commit()
                cursor.close()
            except sql.Error:
                raise EmbeddingWriteError()
        
    def initialize_db(self) -> None:
        """Initializes the table used for storing image embeddings.
        
            Raises:
                EmbeddingDBInitError: if there was an sqlite3 error when initializing the database.
        """
        try:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS embeddings 
                            (name TEXT,
                            embedding BLOB PRIMARY KEY)""")
            self.conn.commit()

        except sql.Error:
            raise EmbeddingDBInitError()


    def close(self) -> None:
        """Closes the connection to the database.

            Raises:
                CloseDataBaseError: if there was an sqlite3 error when closing the database.    
        
        """
        try:
            self.conn.close()
        except sql.Error:
            raise CloseDBError()

    def check_table_exist(self) -> bool:
        """Checks if db exists.
        
            Returns:
                bool: True if database exists.
        
        """
        cursor = self.conn.cursor()
        db = cursor.execute("SELECT name FROM sqlite_master WHERE name = 'embeddings'")
        if db.fetchone() is None:
            return False
        return True

    def check_embedding(self, embedding: np.ndarray) -> bool:
        """Checks if an embeddings is in db.

            Args:
                embedding (np.ndarray): embedding which will be checked.

            Returns:
                bool: True if embedding is already in the db.

        """
        if embedding is None:
            raise TypeError("Embedding is None")
        cursor = self.conn.cursor()
        cursor.execute("SELECT embedding FROM embeddings WHERE embedding = ?", (embedding.tobytes(),))
        result = cursor.fetchone()
        if result:
            return True
        return False
    
    def change_embedding_name(self, embedding: np.ndarray, name: str) -> None:
        try:
            cursor = self.conn.cursor()

            cursor.execute("UPDATE embeddings SET name = ? WHERE embedding = ?", (name, embedding))
            self.conn.commit()

        except sql.Error:
            raise ChangeEmbeddingNameError()
