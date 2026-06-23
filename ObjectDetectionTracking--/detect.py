from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    # Object detection + tracking
    results = model.track(frame, persist=True)

    # Draw boxes
    annotated_frame = results[0].plot()

    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press ESC to close
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()