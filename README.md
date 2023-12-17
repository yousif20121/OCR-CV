# Image & Video OCR
 
### Image OCR using Tesseract

This Python script performs Optical Character Recognition (OCR) on an image using the Tesseract OCR engine. The script uses the `pytesseract` library along with the OpenCV and Pillow libraries for image processing and display.

#### Prerequisites

- Python 3.x
- Tesseract OCR installed ([Download Tesseract](https://github.com/tesseract-ocr/tesseract))
- Required Python packages: `pytesseract`, `Pillow`, `opencv-python`

#### Setup

1. Install the required Python packages:

   ```bash
   pip install pillow pytesseract opencv-python
   ```

2. Set the Tesseract executable path in the script:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

   Replace the path with the correct location of your Tesseract executable.

#### Usage

1. Adjust the `filename` variable to point to the image you want to process.

2. Run the script:

   ```bash
   python image_ocr.py
   ```

#### Features

- Extracts text from an image using Tesseract OCR.
- Filters out text with confidence less than 40.
- Displays the image with bounding boxes around recognized text.

---

### Video OCR using Tesseract

This Python script performs Optical Character Recognition (OCR) on a video file using the Tesseract OCR engine. The script uses the `pytesseract`, `opencv-python`, and `Pillow` libraries for OCR, video processing, and display.

#### Prerequisites

- Python 3.x
- Tesseract OCR installed ([Download Tesseract](https://github.com/tesseract-ocr/tesseract))
- Required Python packages: `pytesseract`, `Pillow`, `opencv-python`

#### Setup

1. Install the required Python packages:

   ```bash
   pip install pillow pytesseract opencv-python
   ```

2. Set the Tesseract executable path in the script:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

   Replace the path with the correct location of your Tesseract executable.

#### Usage

1. Adjust the `video_path` variable to point to the video file you want to process.

2. Run the script:

   ```bash
   python video_ocr.py
   ```

3. Press 'q' to exit the video display.

#### Features

- Processes a video file and performs OCR on selected frames.
- Skips frames to speed up processing (adjustable with `skip_frames`).
- Displays the video with annotated text using bounding boxes.
