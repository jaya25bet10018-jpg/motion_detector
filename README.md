Project Title--Real-Time Motion Detection and Occupancy Monitoring Using Python
 #Overview of the Project
This project is a real-time motion detection and occupancy monitoring system built using Python and OpenCV. It captures live video using a webcam, detects motion by comparing video frames, and highlights detected motion areas with bounding boxes. A binary mask (foreground mask) is also generated to visually represent detected movement.
The system determines whether the room is occupied based on motion and displays the status on the video feed. This project demonstrates essential concepts of computer vision such as frame differencing, thresholding, contour detection, and background subtraction.
A sample screenshot from the project execution is shown below:

#Features:-
Real-time motion detection using webcam feed
Background subtraction for isolating moving objects
Binary mask visualization of detected motion
Red bounding boxes drawn around detected motion regions
Automatic room occupancy detection
Lightweight and easy to understand
Extensible for security systems or gesture-based applications
#Tools Used:-
Python 3.x
OpenCV (cv2)
NumPy
IDE: PyCharm / VS Code (optional)
Webcam (built-in or external)

#Steps to Install & Run the Project
Clone the Repository
git clone https://github.com/yourusername/motion-detection-python.git
cd motion-detection-python

#Install Required Dependencies
pip install opencv-python numpy
Run the Project
python motion_detection.py
Ensure your webcam is connected and accessible.
#Instructions for Testing
To test the motion detection system:
Start the program — the webcam feed will open.
Move your hand or any object in front of the camera.
You should see:
Red bounding boxes around moving areas
White foreground mask in the processing window
Room Status: Occupied displayed when motion is detected
Stay still — the system should detect no motion and update accordingly.
Test in different lighting conditions to observe accuracy.
