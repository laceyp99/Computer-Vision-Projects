import cv2
import mediapipe as mp
from collections import deque
import time

# Initialize MediaPipe Hands
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Global variables for volume control
volume_mode = False
prev_y_vals = deque(maxlen=5)
last_change_time = 0
volume_level = 50  # Start at midpoint

def count_fingers(hand_landmarks):
    # Tip landmarks for each finger (excluding thumbs to keep it simple and allow for either hand to be used)
    tips = [8, 12, 16, 20]
    fingers = 0

    for tip in tips:
        # Compare tip to the pip joint (tip - 2)
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers += 1

    return fingers

def update_volume(current_y):
    global last_change_time, volume_level

    if len(prev_y_vals) == 5:
        delta = prev_y_vals[0] - current_y  # + = up, - = down

        if abs(delta) > 20 and time.time() - last_change_time > 0.2:
            if delta > 0:
                volume_level = min(100, volume_level + 3)
            else:
                volume_level = max(0, volume_level - 3)
            last_change_time = time.time()
            # print("Volume:", volume_level)

    prev_y_vals.append(current_y)

# Main loop to capture video and process hand gestures
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # frame = cv2.flip(frame, 1)  # Mirror image
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get y of wrist (landmark 0)
                wrist_y = hand_landmarks.landmark[0].y  # Normalized 0–1
                h, w, _ = frame.shape
                wrist_pixel_y = int(wrist_y * h)
                cv2.putText(frame, f"Wrist Y: {wrist_pixel_y}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Count fingers
                fingers_up = count_fingers(hand_landmarks)
                
                # Check for "1 finger" gesture to enter volume control mode
                if fingers_up == 1:
                    volume_mode = True
                    update_volume(wrist_pixel_y)
                    cv2.putText(frame, f"VOLUME MODE ({volume_level})", (10, 100),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    volume_mode = False
                    prev_y_vals.clear()

        cv2.imshow("Hand Tracker", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()