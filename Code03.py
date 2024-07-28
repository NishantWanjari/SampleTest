import cv2
import dlib
import numpy as np

# Load the image
image_path = 'Low Resolution.jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained facial landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dlib.shape_predictor('shape_predictor_68_face_landmarks_GTX.dat'))

# Detect faces
faces = detector(gray)
if len(faces) == 0:
    print("No face detected")
    exit()

# Assuming the first detected face
face = faces[0]
landmarks = predictor(gray, face)

# Extract landmarks
points = []
for i in range(68):  # 68 facial landmarks
    x = landmarks.part(i).x
    y = landmarks.part(i).y
    points.append((x, y))

points = np.array(points)
