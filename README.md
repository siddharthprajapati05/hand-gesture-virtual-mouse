# Hand Gesture Virtual Mouse

A Python project that allows you to control your computer mouse using hand gestures via your webcam.  
Uses **MediaPipe** for hand tracking, **OpenCV** for webcam capture, and **PyAutoGUI** for controlling the mouse.

---

## Features

- Move the cursor using the index finger
- Click using thumb + index finger
- Scroll up using index + middle fingers
- Scroll down using ring + pinky fingers
- Disable cursor movement when making a fist

---

## Requirements

- Python 3.8+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)

Install dependencies with:

```bash
pip install -r requirements.txt


Activate your virtual environment:
source venv/bin/activate   # Mac/Linux
# or
.\venv\Scripts\activate    # Windows

python virtual_mouse.py


hand-gesture-virtual-mouse/
│
├── venv/                 # Virtual environment (ignored in Git)
├── virtual_mouse.py      # Main Python script
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

