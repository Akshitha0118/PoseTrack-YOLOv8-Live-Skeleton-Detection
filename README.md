# 🚀 PoseTrack-YOLOv8-Live-Skeleton-Detection

## 📌 Project Overview

This project implements a real-time human pose estimation system using YOLOv8 Pose model and OpenCV.
The system captures video (webcam or uploaded file), detects humans, and identifies 17 key body landmarks (shoulders, elbows, knees, etc.) in real time.
This demonstrates end-to-end integration of deep learning models into a live computer vision pipeline.
---
## 🧠 Tech Stack

Python

YOLOv8 Pose (Ultralytics)

OpenCV

Deep Learning (CNN-based architecture)
---
## 🔥 Key Features

- Real-time video processing
- 17 human keypoint detection
- Skeleton visualization
- Lightweight and fast inference
- Easy-to-deploy architecture
---
## 🏗️ System Architecture

Video Input → Frame Capture → YOLOv8 Pose Model →
Keypoint Detection → Skeleton Rendering → Real-Time Display
---
## ⚙️ Installation
pip install ultralytics opencv-python
### ▶️ How to Run
python app.py

Press q to exit.

### 📊 How It Works

Capture frame using OpenCV

Pass frame to YOLOv8 pose model

Model extracts spatial features using CNN backbone
---
## Predicts:

Bounding boxes

Confidence scores

17 human keypoints

Skeleton connections are drawn

Output displayed in real time
---
## 🎯 Real-World Applications

🏋️ Fitness posture correction

🧘 Yoga pose analysis

⚽ Sports performance tracking

🤖 Robotics motion understanding

🏢 Workplace ergonomic monitoring

---
## 📈 Performance

Real-time inference (hardware dependent)

Works on CPU (basic performance)

Optimized performance with GPU

---
# 👩‍💻 Author

## Akshitha Hirakari
## Aspiring Computer Vision & AI Engineer
