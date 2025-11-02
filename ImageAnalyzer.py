import cv2 as cv
from insightface.app import FaceAnalysis
import numpy as np
from PySide6.QtGui import QImage, QPixmap

def cv_image_to_qpixmap(cv_image: np.ndarray):  
    rgb_image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)

    height, width, channels = rgb_image.shape
    bytes_per_line = channels * width

    q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

    return QPixmap.fromImage(q_image)

class ImageAnalyzer:
    def __init__(self) -> None:
        self.app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
        self.app.prepare(ctx_id=-1)
    
    # gets the face embedding of all of the faces inside of the image
    def get_faces(self, image_path: str) -> list:
        image = cv.imread(image_path)

        if image is None:
            raise ValueError(f"Could not read {image_path}")
        
        faces = self.app.get(image)

        if len(faces) < 1:
            raise ValueError("No faces detected in image")

        return faces
    
    def check_same_face(self, emb1, emb2, threshold=.7) -> bool:
        similarity =  np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        return similarity / threshold
    
    # draws a rectangle around the head of the inputed face
    def draw_box_around_face(self, image_path: str, face: np.ndarray):
        image = cv.imread(image_path)

        if image is None:
            raise ValueError("Image failed to load")
        if face is None:
            raise ValueError("error occured with face object")
        x1, y1, x2, y2 = face.astype(int)

        image = cv.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

        return image


if __name__ == "__main__":
    image_path = "venv\\IMG_20250602_182834737.jpg"
    analyzer = ImageAnalyzer()
    faces = analyzer.get_faces(image_path)
    image = analyzer.draw_box_around_face(image_path, faces[0].bbox)


    cv.imshow("TEST", image)
    cv.waitKey(0)
    cv.destroyAllWindows()