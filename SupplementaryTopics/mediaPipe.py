import cv2
import mediapipe as mp


mp_pose = mp.solutions.pose
pose_landmarker = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose_landmarker.process(rgb_frame)

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        connections = mp_pose.POSE_CONNECTIONS
        for connection in connections:
            start_idx, end_idx = connection
            start_point = tuple(map(int, (results.pose_landmarks.landmark[start_idx].x * frame.shape[1],
                                          results.pose_landmarks.landmark[start_idx].y * frame.shape[0])))
            end_point = tuple(map(int, (results.pose_landmarks.landmark[end_idx].x * frame.shape[1],
                                        results.pose_landmarks.landmark[end_idx].y * frame.shape[0])))
            cv2.line(frame, start_point, end_point, (255, 0, 0), 2)


    cv2.imshow('pose landmark', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()