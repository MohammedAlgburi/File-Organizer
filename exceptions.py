class EncodingManagerError(Exception):
    """General exception for the face encoding database module"""
    pass

class EncodingWriteError(EncodingManagerError):
    """Raised when an error occurs while writting encodings into the database."""
    def __init__(self, message = "An error occured while writing to the encoding database") -> None:
        super().__init__(message)

class EncodingDBInitError(EncodingManagerError):
    """Raised when an error occurs while initializing the database"""
    def __init__(self, message = "An error occured while initializing the database") -> None:
        super().__init__(message)



