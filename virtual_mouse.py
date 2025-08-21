import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Get screen size
screen_w, screen_h = pyautogui.size()

# Variables for fist detection
cursor_enabled = True
last_x, last_y = None, None

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Get finger landmarks
            index_finger = lm[8]
            thumb = lm[4]
            middle_finger = lm[12]
            ring_finger = lm[16]
            pinky = lm[20]

            h, w, _ = frame.shape
            x, y = int(index_finger.x * w), int(index_finger.y * h)

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect fist (all fingers folded)
            fist = (index_finger.y > lm[6].y and
                    middle_finger.y > lm[10].y and
                    ring_finger.y > lm[14].y and
                    pinky.y > lm[18].y)

            if fist:
                cursor_enabled = False
            else:
                if not cursor_enabled:  # Re-enable cursor when hand opens
                    cursor_enabled = True
                    last_x, last_y = None, None

            # Move cursor with index finger
            if cursor_enabled:
                screen_x = int(index_finger.x * screen_w)
                screen_y = int(index_finger.y * screen_h)

                if last_x is not None and last_y is not None:
                    pyautogui.moveTo(screen_x, screen_y, duration=0.1)  # Smooth movement
                last_x, last_y = screen_x, screen_y

            # Detect click (index and thumb close)
            if abs(index_finger.x - thumb.x) < 0.05 and abs(index_finger.y - thumb.y) < 0.05:
                pyautogui.click()

            # Scroll up (index + middle up)
            if index_finger.y < lm[6].y and middle_finger.y < lm[10].y:
                pyautogui.scroll(50)  # Smooth slow scroll up

            # Scroll down (ring + pinky up)
            if ring_finger.y < lm[14].y and pinky.y < lm[18].y:
                pyautogui.scroll(-50)  # Smooth slow scroll down

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
