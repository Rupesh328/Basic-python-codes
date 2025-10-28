import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe and pyautogui
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Get screen size for cursor scaling
screen_width, screen_height = pyautogui.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                if id == 8:  # Index finger tip (id=8 in Mediapipe hand model)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    # Convert hand coordinates to screen coordinates
                    screen_x = screen_width / w * cx
                    screen_y = screen_height / h * cy

                    # Move the mouse cursor
                    pyautogui.moveTo(screen_x, screen_y)

            # Draw hand landmarks on the video frame
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
