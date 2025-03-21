import cv2
import face_recognition
import numpy as np
import csv
import os
from datetime import datetime


image_dir = "C:\\Users\\harsh\\for github\\known_images"
attendance_file = "C:\\Users\\harsh\\for github\\attendance_sheet.csv"


known_face_encodings = []
known_face_names = []

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_dir, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)

        if encoding:
            known_face_encodings.append(encoding[0])
            known_face_names.append(os.path.splitext(filename)[0])  


system_id = input("Enter your System ID: ")

if system_id not in known_face_names:
    print("No face data found for this System ID. Try again!")
    exit()

print("Scanning... Look into the camera!")


cap = cv2.VideoCapture(0)
attendance_marked = False

while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances) if face_distances.size else None
        name = "Unknown"

        if best_match_index is not None and matches[best_match_index]:
            name = known_face_names[best_match_index]

        
        top, right, bottom, left = face_location
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        
        if name == system_id and not attendance_marked:
            print(f"✅ Attendance marked for {system_id}")

            
            with open(attendance_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([system_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

            attendance_marked = True
            break  

    cv2.imshow("Face Recognition Attendance System", frame)

    if attendance_marked or cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
