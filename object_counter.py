import cv2
from ultralytics import YOLO, solutions

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("C:/Users/lenovo/Desktop/Vidéos/object_counting.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH,
                                       cv2.CAP_PROP_FRAME_HEIGHT,
                                       cv2.CAP_PROP_FPS))

line_points = [(0, 400), (2000, 400)]  # line or region points
classes_to_count = [2]  # car classes for count

# Video writer
video_writer = cv2.VideoWriter("object_counting_output.avi",
                               cv2.VideoWriter_fourcc(*"mp4v"),
                               fps,
                               (w, h))

# Init Object Counter
counter = solutions.ObjectCounter(
    view_img=True,
    reg_pts=line_points,
    classes_names=model.names,
    draw_tracks=True,
    line_thickness=2,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing"
              " has been successfully completed.")
        break
    tracks = model.track(im0,
                         persist=True,
                         show=False,
                         classes=classes_to_count)

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
