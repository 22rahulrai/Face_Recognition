# Face Recognition Attendance System 🎯

This project is a Python-based **Face Recognition Attendance System** that uses OpenCV for face detection and recognition, K-Nearest Neighbors (KNN) for classification, and SQLite + CSV for attendance data storage. It also includes voice feedback using the Windows Speech API.

---

## 🔍 Features

- 📸 Real-time **face detection** using Haar Cascades.
- 🧠 Face **recognition** with KNN classifier from `scikit-learn`.
- 📋 **Attendance tracking** with name and timestamp saved to CSV.
- 🔊 **Voice feedback** when attendance is successfully taken.
- 💾 SQLite database integration to store face encodings and names.

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **scikit-learn**
- **NumPy**
- **SQLite3**
- **Windows Speech API (SAPI)**
- **CSV**

---

## ⚙️ How It Works

1. **Face Registration**:
   - Captures 50 face samples per person.
   - Saves their name and image encoding into `.pkl` files and an SQLite database.

2. **Face Recognition & Attendance**:
   - Captures real-time video feed from webcam.
   - Detects and recognizes known faces using the trained KNN model.
   - On pressing **`O`**, it logs the name and timestamp into a dated CSV file inside the `/Attendance` folder.
   - On pressing **`Q`**, it quits the application.

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- Webcam
- Windows (for voice functionality)

### 📦 Installation

```bash
git clone https://github.com/22rahulrai/Face_Recognition.git
cd Face_Recognition
pip install -r requirements.txt


├── data/
│   ├── faces_data.pkl
│   └── names.pkl
├── Attendance/
│   └── Attendance_<date>.csv
├── database.db
├── haarcascade_frontalface_default.xml
├── register_face.py
├── face_attendance.py
├── README.md
└── requirements.txt

Attendance_24-04-2025.csv
--------------------------
| NAME     | TIME        |
|----------|-------------|
| Rahul    | 10:42-12    |

```
## 🧠 Future Enhancements
- Use Deep Learning (e.g., FaceNet, Dlib) for better recognition.
- Add a web interface using Flask or Django.
- Implement duplicate entry prevention.


