

import cv2
from ultralytics import YOLO

# 1. Load YOLOv8 model
model = YOLO("yolov8n.pt")q

# 2. Initialize webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

# 3. Process frames continuouslyqqqqqqq
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # 4. Run YOLOv8 detection
    results = model(frame)

    # 5. Annotate frame with bounding boxes & labels
    annotated_frame = results[0].plot()

    # 6. Display the annotated frame
    cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 7. Cleanup
cap.release()
# cv2.destroyAllWindows()