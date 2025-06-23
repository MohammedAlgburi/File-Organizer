import face_recognition
import cv2 as cv
import sys

def get_face_encodings(image_path: str):
    image = face_recognition.load_image_file(image_path)

    list_of_face_encodings = face_recognition.face_encodings(image)
    print(list_of_face_encodings)

def show_cropped_face(coordinates: tuple):
    pass
