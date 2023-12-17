from PIL import Image
import pytesseract
import numpy as np
from pytesseract import Output
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the video file
video_path = 'Testing Material/1.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Set the desired window size
window_width = 800
window_height = 600

# Set the number of frames to skip
skip_frames = 5  # Adjust this value to skip more or fewer frames

frame_count = 0

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Skip frames if needed
    if frame_count % skip_frames != 0:
        continue

    # Perform OCR on the frame
    text_full = pytesseract.image_to_string(frame)

    # Perform OCR with detailed results
    results = pytesseract.image_to_data(frame, output_type=Output.DICT)

    for i in range(0, len(results["text"])):
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        text_single = results["text"][i]
        conf = int(results["conf"][i])
        if conf > 40:
            text_single = "".join([c if ord(c) < 128 else "" for c in text_single]).strip()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text_single, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

    # Resize the frame to the desired window size
    frame = cv2.resize(frame, (window_width, window_height))

    # Display the frame with OCR results
    cv2.imshow("Video OCR", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
