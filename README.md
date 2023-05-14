

# Student Registration and Face Recognition using Harcascade and LBPH

This project is a Python-based student registration and face recognition system. The project uses two popular algorithms: Harcascade and LBPH (Local Binary Pattern Histogram) to recognize faces and verify them against a pre-existing student database.

The system features a graphical user interface (GUI) built using the Tkinter library in Python, which provides an easy-to-use interface for users to input and retrieve information.

## Installation

Before running the project, make sure you have the following dependencies installed:

* Python 3.x
* OpenCV
* Numpy
* Tkinter

To install these dependencies, you can use pip:

```bash
pip install opencv-python numpy tkinter
```

## How to use

1. Clone the repository:

```bash
git clone https://github.com/<username>/student-registration-and-face-recognition.git
```

2. Navigate to the project directory:

```bash
cd student-registration-and-face-recognition
```

3. Run the project:

```bash
python main.py
```

4. The GUI will appear, providing you with the following options:

* Register New Student: This allows you to register a new student by entering their name, ID, and taking a picture of their face.
* Recognize Student: This allows you to recognize a student by taking a picture of their face and verifying it against the pre-existing student database.

## How it works

### Registering a new student

When you click the "Register New Student" button in the GUI, you will be prompted to enter the student's name and ID. Once you have entered this information, the system will open your webcam and prompt you to take a picture of the student's face.

The system will then use the Harcascade algorithm to detect the face in the image and crop it to the appropriate size. The LBPH algorithm is then used to generate a histogram of the face, which is saved to the pre-existing student database along with the student's name and ID.

### Recognizing a student

When you click the "Recognize Student" button in the GUI, the system will again open your webcam and prompt you to take a picture of the student's face. The Harcascade algorithm is used to detect the face in the image and crop it to the appropriate size.

The LBPH algorithm is then used to generate a histogram of the face, which is compared to the histograms of all the students in the pre-existing student database. If there is a match, the system will display the name and ID of the recognized student in the GUI.

## Conclusion

This project provides an easy-to-use student registration and face recognition system using the Harcascade and LBPH algorithms. The graphical user interface built using the Tkinter library makes it easy for users to input and retrieve information.
 
