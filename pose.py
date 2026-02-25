import cv2
from ultralytics import YOLO

# Load YOLOv8 Pose model
model = YOLO('yolov8n-pose.pt')

# 🔹 Path to your video file
video_path = r'C:\Users\Admin\Desktop\YOLO_POSE\From Main Klickpin CF- Pinterest Video - 1IqkLYm2N.mp4'
# Open video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties (for saving output)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Save output video
out = cv2.VideoWriter(
    "pose_output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Finished processing video.")
        break

    # Perform pose estimation
    results = model(frame)

    # Annotate frame with keypoints
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLOv8 Pose Estimation - Video", annotated_frame)

    # Save output frame
    out.write(annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()