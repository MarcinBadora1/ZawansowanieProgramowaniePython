import cv2
import imutils
import time


# model detection
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # przetrenowany model wykrycia ludzi


# metoda detekcji
def detect(frame):
    #bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride = (1, 1), padding = (32, 43), scale = 3.37)
    #bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(3, 3), scale=3.40)
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride= (1, 1), padding= (12, 17), scale=3.40)
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    cv2.putText(frame, 'Status : Wykryto ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Wszyscy osoby : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)
    return frame


def detect_image(image):
    image = imutils.resize(image, width=min(900, image.shape[1]))
    result_image = detect(image)
    cv2.imshow('output', result_image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


def detect_person(image_path):
    if image_path is not None:
        print(f'Otwarto obraz z {image_path}')
        detect_image(image_path)


# zdjęcia
images = [cv2.imread('Images/Person_1.jpg'), cv2.imread('Images/Person_2.jpg'), cv2.imread('Images/Person_3.jpg'),
          cv2.imread('Images/Person_4.jpg'), cv2.imread('Images/Person_5.jpg')]
for image in images:
    start_point = time.time()
    detect_person(image)
    print("Czas na zbadanie %.3f sekund " % (time.time() - start_point))
