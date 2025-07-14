import face_recognition as fr
import cv2 as cv

def process_image(image_path: str) -> tuple:
    image = fr.load_image_file(image_path)

    face_locations = fr.face_locations(image)

    encodings = []

    encodings = fr.face_encodings(image, known_face_locations=face_locations)

    return (face_locations, encodings)

def draw_box_around_face(image_path: str, face_location: tuple):
    image = fr.load_image_file(image_path)

    image_bgr = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    for top, right, bottom, left in face_location:
        cv.rectangle(image_bgr, (left, top), (right, bottom), (0,255,0), 2)

    image = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB)
    return image

if __name__ == "__main__":
    info = process_image("venv\\IMG_20250602_182834737.jpg")
    cv.imshow("Test", draw_box_around_face("venv\\IMG_20250602_182834737.jpg", info[0]))
    cv.waitKey(0)
    cv.destroyAllWindows()