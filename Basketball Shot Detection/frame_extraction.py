import cv2
import os

video_path = "Basketball Shot Detection/video.mp4"
output_folder = "Basketball Shot Detection/frames"
frame_skip = 20  # use every 20th frame to reduce workload

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
i = 0
frame_id = 0

while cap.isOpened():
    # print(f"Processing frame {i}...")
    ret, frame = cap.read()
    if not ret:
        break

    if i % frame_skip == 0:
        filename = os.path.join(output_folder, f"frame_{frame_id:04d}.jpg")
        cv2.imwrite(filename, frame)
        frame_id += 1

    i += 1

cap.release()