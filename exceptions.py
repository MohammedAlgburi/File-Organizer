class EncodingManagerError(Exception):
    """General exception for the face encoding database"""
    pass

class EncodingWriteError(EncodingManagerError):
    """Raised when an error occurs while writting encodings into the database."""
    def __init__(self, message = "An error occured while writing to the encoding database") -> None:
        super().__init__(message)

class EncodingDBInitError(EncodingManagerError):
    """Raised when an error occurs while initializing the database"""
    def __init__(self, message = "An error occured while initializing the database") -> None:
        super().__init__(message)

class CloseDataBaseError(EncodingManagerError):
    """Raised when an error occurs while closing the connection to the database"""
    def __init__(self, message = "An error occured while closing the database") -> None:
        super().__init__(message)

class FileManagerError(Exception):
    """General exception for the File manager class"""
    pass

class NotDirectoryError(FileManagerError):
    """Raised when a file path is not a directory."""
    def __init__(self, message = "Inputted file path is not a directory") -> None:
        super().__init__(message)



