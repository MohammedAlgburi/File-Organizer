import face_recognition as fr
import cv2 as cv
import numpy as np

def process_image(image_path: str) -> tuple:
    image = fr.load_image_file(image_path)

    face_locations = fr.face_locations(image)

    encodings = []

    for face in face_locations:
        encodings = fr.face_encodings(image, known_face_locations=face)
    
    return (face_locations, encodings)
