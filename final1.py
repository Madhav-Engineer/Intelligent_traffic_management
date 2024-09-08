import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import Tracker
from t1 import control_traffic_signal1,control_traffic_signal2

def process_frame(cap, model, tracker,class_list):
    ret, frame = cap.read()
    if not ret:
        return None, 0  # No frame captured, return None and 0 vehicles
    
    frame = cv2.resize(frame, (510, 250))  # Resize to fit the quadrant
    results = model.predict(frame)
    px = pd.DataFrame(results[0].boxes.data).astype("float")

    vehicle_list = []
    vehicle_count = 0  # Initialize vehicle count for this frame
    for index, row in px.iterrows():
        x1, y1, x2, y2, _, d = row
        if class_list[int(d)] == 'car':  # Assuming 'car' is the label for vehicles
            vehicle_list.append([int(x1), int(y1), int(x2), int(y2)])
            vehicle_count += 1
        
    bbox_id = tracker.update(vehicle_list)
    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox
        cx, cy = (x3 + x4) // 2, (y3 + y4) // 2
        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
        cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
        
    return frame, vehicle_count

def main():
    video_paths = [
        'C:\\Users\\geeth\\Downloads\\WhatsApp Video 2024-04-25 at 1.11.07 PM.mp4',
        'C:\\Users\\geeth\\Downloads\\WhatsApp Video 2024-04-25 at 1.11.07 PM (1).mp4',
        'C:\\Users\\geeth\\Downloads\\WhatsApp Video 2024-04-25 at 1.11.07 PM (2).mp4',
        'C:\\Users\\geeth\\Downloads\\WhatsApp Video 2024-04-25 at 1.11.07 PM (3).mp4'
    ]
    
    caps = [cv2.VideoCapture(path) for path in video_paths]
    model = YOLO('yolov8s.pt')
    trackers = [Tracker() for _ in range(4)]
    vehicle_counts = [0, 0, 0, 0]
    my_file = open("coco.txt", "r")
    data = my_file.read()
    class_list = data.split("\n") 
    first_time=True
    while True:
        
        frames_and_counts = [process_frame(cap, model, tracker,class_list) for cap, tracker in zip(caps, trackers)]
        frames = [fc[0] for fc in frames_and_counts if fc[0] is not None]
        counts = [fc[1] for fc in frames_and_counts if fc[0] is not None]
        vehicle_counts = [0, 0, 0, 0]
        if len(frames) < 4:  # Check if any frame is None (video ended)
            break
        
        vehicle_counts = [sum(x) for x in zip(vehicle_counts, counts)]
        print("vehicle_counts",vehicle_counts)
       
        top_row = cv2.hconcat([frames[0], frames[1]])
        bottom_row = cv2.hconcat([frames[2], frames[3]])
        combined_frame = cv2.vconcat([top_row, bottom_row])
        
        for idx, count in enumerate(vehicle_counts):
            pos = [(10, 20), (530, 20), (10, 270), (530, 270)][idx]
            cv2.putText(combined_frame, f'Vehicles: {count}', pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        cv2.imshow("Four Video Streams", combined_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if (first_time==True):
            max_tie_lanes,max_lane,cars1,lights,lanes,green_signal=control_traffic_signal1(vehicle_counts)
            first_time=False
        else:
            control_traffic_signal2(vehicle_counts,max_tie_lanes,max_lane,cars1,lights,lanes,green_signal)
    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()
    return 
    

if __name__ == "__main__":
    main()
    

