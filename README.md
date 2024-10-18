Face Recognition Attendance System 

This project implements a Face Recognition Attendance System using Python, OpenCV, and machine learning algorithms.
The system can detect faces from a webcam, recognize them using a K-Nearest Neighbors (KNN) model, and automatically 
mark attendance in a CSV file along with a timestamp.

Key Features:
    Real-time Face Detection: Detects faces using OpenCV’s Haar Cascade classifier.
    Face Recognition: Uses a pre-trained KNN classifier to identify faces from the webcam.
    Attendance Management: Automatically logs the name and timestamp of recognized individuals in a CSV file.
    Text-to-Speech: Provides audio feedback when attendance is recorded using the Windows Speech API.
    SQLite Database Integration: Stores face encodings and associated names in an SQLite database for future use.

Technologies Used:
    Python: Core programming language for building the system.
    OpenCV: Used for capturing and processing images from the webcam.
    scikit-learn (KNN): Machine learning model for face recognition.
    SQLite: Database to store face encodings and names.
    CSV: Used for attendance recording.
    Windows Speech API: Provides voice feedback after attendance is logged.

How It Works:
    Capture face images and save their encodings in the database.
    Train a KNN model using the saved face data.
    Detect and recognize faces in real-time.
    Log the recognized person’s name and timestamp into a CSV file upon pressing a specific key.
    Voice confirmation is given when attendance is recorded.


