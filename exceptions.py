class EmbeddingManagerError(Exception):
    """General exception for the face encoding database"""
    pass

class EmbeddingWriteError(EmbeddingManagerError):
    """Raised when an error occurs while writting encodings into the database."""
    def __init__(self, message = "An error occured while writing to the encoding database") -> None:
        super().__init__(message)

class EmbeddingDBInitError(EmbeddingManagerError):
    """Raised when an error occurs while initializing the database"""
    def __init__(self, message = "An error occured while initializing the database") -> None:
        super().__init__(message)

class CloseDBError(EmbeddingManagerError):
    """Raised when an error occurs while closing the connection to the database"""
    def __init__(self, message = "An error occured while closing the database") -> None:
        super().__init__(message)

class ChangeEmbeddingNameError(EmbeddingManagerError):
    """Raised when an error occurs while changing an embedding's name"""
    def __init__(self, message= "An error occured while changing embedding name") -> None:
        super().__init__(message)

class FileManagerError(Exception):
    """General exception for the File manager class"""
    pass




