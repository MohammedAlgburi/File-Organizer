from pathlib import Path

IMAGE_EXTENSIONS = ["*.png", "*.jpg", "*.jpeg"]

def get_image_from_dir(p: Path) -> list:
    image_file_paths = []
    
    # grabs file names which end in png, jpg or jpeg
    for ext in IMAGE_EXTENSIONS:
        image_file_paths.extend(p.rglob(ext))

    return image_file_paths
