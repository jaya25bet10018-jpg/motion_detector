This project is a simple motion detection system designed to identify movement in front of a camera and respond to it in real time. The main goal is to create an easy-to-understand solution that can be used for security, automation, or basic computer-vision learning.

#Features
Real-time video capture and frame processing
Automatic motion detection using frame differencing
Grayscale conversion and Gaussian smoothing for noise reduction
Status text updates (e.g., "Occupied" / "Unoccupied")
Records timestamps of detected motion
Lightweight and easy to extend for security applications

 #Tools Used:-
Python 3
OpenCV (cv2) – image processing & video capture
imutils – frame resizing & basic utilities
datetime – timestamp generation
time – controlling frame processing

Steps to Install & Run the Project
1. Clone or Download the Project
   git clone https://github.com/yourusername/motion-detector.git
   cd motion-detector
2. Install Required Libraries:-
   pip install opencv-python imutils
3. Run the Script:-
   python motion_detector.py
4. Exit:-
   Press Q to quit the live window.

Instructions for Testing
Ensure your laptop/PC webcam is connected and functioning.
Start the program and stay out of the frame for the first few seconds — this helps the system capture the reference frame.
Move your hand or walk in front of the camera to generate motion.
The system will display changes and update the status accordingly.
Check the console or list for timestamps of when motion occurred.
