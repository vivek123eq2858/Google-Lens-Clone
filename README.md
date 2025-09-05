# Google Lens Clone - 

This project is a **Google Lens Clone** built with Python. It allows users to capture live video from a **laptop webcam** or **mobile phone camera**, detect **text (OCR)** and **objects (YOLOv8)** in real-time, and directly search the results on **Google**.

---

## 🚀 Features
- Live video stream from:
  - Laptop webcam
  - Mobile camera (via IP webcam app)
- **Text Detection** using [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- **Object Detection** using [YOLOv8](https://github.com/ultralytics/ultralytics)
- One-click **Google Search** for detected text and objects
- User-friendly **Tkinter GUI**

---

## 📂 Project Structure
GoogleLensClone/
│── google_lens_clone.py # Main application file
│── README.md # Project documentation


---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Google-Lens-Clone.git
cd Google-Lens-Clone

2. Install Dependencies

Make sure you have Python 3.8+ installed. Then install required packages:

pip install opencv-python pillow numpy easyocr ultralytics

3. (Optional) Mobile Camera Setup

Install IP Webcam app (Android) or similar app (iOS alternatives available).

Start the server in the app → copy the stream URL (e.g., http://192.168.1.2:8080/video).

Replace the self.mobile_url in the code with your IP webcam URL.

▶️ Usage

Run the app with:

python google_lens_clone.py

In the GUI:

Choose Laptop or Mobile camera source.

Click Detect Text & Objects → performs OCR + Object Detection.

Click Search on Google to search detected content.

📸 Demo (Steps)

Start app → live camera feed appears.

Capture frame → detects text & objects.

Display result in entry box + label.

Google search opens with one click.

⚡ Tech Stack

Python

OpenCV (video processing)

Tkinter (GUI)

Pillow (image conversion for Tkinter)

EasyOCR (text recognition)

YOLOv8 (Ultralytics) (object detection)

Threading (non-blocking detection)

📝 Notes

Works best in well-lit environments.

For OCR, English (['en']) is enabled. You can add more languages if needed:

ocr_reader = easyocr.Reader(['en', 'hi'])


Object detection model is yolov8n.pt (lightweight). You can replace with yolov8s.pt or larger models for better accuracy.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by [Your Name] 🚀


---

👉 Now you can copy these two files (`google_lens_clone.py` and `README.md`) into your project folder and push them to GitHub.  

Do you want me to also create a **requirements.txt** file for this project so installation becomes one command (`pip install -r requirements.txt`)?
