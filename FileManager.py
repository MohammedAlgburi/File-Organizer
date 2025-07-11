from pathlib import Path
from exceptions import NotDirectoryError

image_extensions = ["*.png", "*.jpg", "*.jpeg"]

class FileManager:
    def __init__(self) -> None:
        self.image_files = []

    def get_image_from_dir(self, dir: str):
        p = Path(dir)
        if p.is_dir() == False:
            raise NotDirectoryError()
        
        # grabs file names which end in png, jpg or jpeg
        for ext in image_extensions:
            self.image_files.extend(p.rglob(ext))
        
        
        
        
