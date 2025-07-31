from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_animal(image):
    results = model.predict(source=image, verbose=False)[0]
    for box in results.boxes:
        label = results.names[int(box.cls)]
        if label in ['dog', 'cat', 'bird', 'horse', 'cow', 'sheep']:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            crop = image[y1:y2, x1:x2]
            return crop
    return None
