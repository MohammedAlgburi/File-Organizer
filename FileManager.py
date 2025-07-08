from pathlib import Path
from exceptions import NotDirectoryError

class FileManager:
    def __init__(self) -> None:
        pass

    def get_image_from_dir(self, dir: str):
        p = Path(dir)
        if p.is_dir() == False:
            raise NotDirectoryError()
        
        
        
