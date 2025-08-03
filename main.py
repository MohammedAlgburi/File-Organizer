# from FaceEmbeddingStorage import FaceEmbeddingStorage
from MainWindow import App
from ImageAnalyzer import ImageAnalyzer, cv_image_to_qpixmap
# from FileManager import FileManager

image_path = "venv\\IMG_20250602_182834737.jpg"

if __name__ == "__main__":
    app = App()
    image_analyzer = ImageAnalyzer()
    # file_manager = FileManager()
    # face_embedding_storage = FaceEmbeddingStorage()