import face_recognition
import cv2 as cv
import numpy as np

def get_face_encodings(image_path: str) -> list[np.ndarray]:
    image = face_recognition.load_image_file(image_path)

    encodings = face_recognition.face_encodings(image)
    print(encodings)
    return encodings

def show_cropped_face(coordinates: tuple):
    pass
