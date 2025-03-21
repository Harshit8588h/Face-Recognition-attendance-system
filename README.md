# Face-Recognition-attendance-system
<br>
Author - Harshit Sangwan



About the Project:

This is a real-time face recognition attendance system that captures a user's face using a webcam, verifies it against stored images, and logs attendance with a timestamp. It integrates OpenCV, face_recognition, and NumPy for efficient processing.

✨ Features:


1. Face Recognition using pre-stored images
2. Automatic Attendance Marking in a CSV file
3. Real-Time Detection via webcam
4. User Identification with name display
5. Simple & Fast Execution

🛠️ Technologies Used:


1. Python 
2. OpenCV (for image processing)
3. face_recognition (for facial recognition)
4. NumPy (for numerical operations)
5. CSV Handling (for attendance tracking)


`Project Structure:


Face Recognition Attendance System


│-- 📂 known_images/       # Folder containing images of registered users


│-- 📄 attendance_system.py # Main Python script


│-- 📄 attendance_sheet.csv # Logs attendance records


│-- 📜 README.md           # Project Documentation

`How to Run the Project:


🔹 Prerequisites


Ensure you have Python installed and install required libraries:

pip install opencv-python face-recognition numpy

🔹 Run the Code:

python attendance_system.py


The webcam will open and start recognizing faces!

How Attendance Works:


- The program captures real-time video from the webcam.
- It compares detected faces with stored images in the known_images folder.
- If a match is found, it logs attendance with a timestamp in attendance_sheet.csv.
- If no match is found, it displays "Unknown" and does not mark attendance.

Sample Output:


✅ Recognized Face

John Doe recognized at 2025-03-21 10:15:30

Unrecognized Face


Unknown detected. No attendance marked.


`Future Improvements:
1. GUI Integration using Tkinter or PyQt
2. Database Storage instead of CSV
3. Multiple Camera Support
4. Face Mask Detection

🤝 Contributing:


Want to improve this project? Fork the repo and submit a pull request! 
