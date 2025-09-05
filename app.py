import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import easyocr
from ultralytics import YOLO
import webbrowser
import urllib.parse
import threading

# Initialize YOLO and EasyOCR
model = YOLO("yolov8n.pt")
ocr_reader = easyocr.Reader(['en'])

class GoogleLensApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Lens Clone - Desktop")
        self.root.geometry("700x700")
        self.root.resizable(False, False)

        self.video_frame = tk.Label(root)
        self.video_frame.pack(pady=10)

        self.source_var = tk.StringVar(value="Laptop")
        self.source_menu = tk.OptionMenu(root, self.source_var, "Laptop", "Mobile", command=self.switch_camera)
        self.source_menu.pack(pady=5)

        self.detect_btn = tk.Button(root, text="Detect Text & Objects", command=self.start_detection_thread)
        self.detect_btn.pack(pady=5)

        self.result_label = tk.Label(root, text="Detected: ", wraplength=600)
        self.result_label.pack(pady=5)

        self.entry = tk.Entry(root, width=60)
        self.entry.pack(pady=5)

        self.search_btn = tk.Button(root, text="Search on Google", command=self.search_google)
        self.search_btn.pack(pady=5)

        # Default to laptop webcam
        self.mobile_url = "http://192.168.1.2:8080/video"  # ← Replace with your phone's IP
        self.cap = cv2.VideoCapture(0)
        self.current_frame = None
        self.detecting = False

        self.update_frame()

    def switch_camera(self, value):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        if value == "Mobile":
            self.cap = cv2.VideoCapture(self.mobile_url)
        else:
            self.cap = cv2.VideoCapture(0)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame.copy()
            resized_frame = cv2.resize(frame, (640, 480))
            cv2image = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def start_detection_thread(self):
        if not self.detecting and self.current_frame is not None:
            self.detecting = True
            threading.Thread(target=self.capture_and_detect, daemon=True).start()

    def capture_and_detect(self):
        frame = self.current_frame

        # OCR preprocessing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        small_gray = cv2.resize(gray, (gray.shape[1]//2, gray.shape[0]//2))
        ocr_result = ocr_reader.readtext(small_gray)
        detected_text = " ".join([text[1] for text in ocr_result])

        # Faster object detection with smaller size
        object_result = model.predict(frame, imgsz=416, verbose=False)[0]
        labels = [model.names[int(box.cls[0])] for box in object_result.boxes]

        combined_result = f"{detected_text} {' '.join(set(labels))}"

        self.root.after(0, self.update_result, combined_result)
        self.detecting = False

    def update_result(self, result):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, result)
        self.result_label.config(text="Detected: " + result)

    def search_google(self):
        query = self.entry.get()
        if query:
            url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
            webbrowser.open(url)

    def __del__(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleLensApp(root)
    root.mainloop()
