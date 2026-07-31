import csv
import os
import time
import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_draw = mp.solutions.drawing_utils


def calculate_angle(a, b, c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(
        c[1] - b[1],
        c[0] - b[0]
    ) - np.arctan2(
        a[1] - b[1],
        a[0] - b[0]
    )

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180:
        angle = 360 - angle

    return angle


cap = cv2.VideoCapture(0)

counter = 0
goal=20
stage = None
exercise = "Bicep Curl"
start_time = time.time()

while True:

    success, frame = cap.read()
   

    if not success:
        break
    elapsed_time = int(time.time() - start_time)

    minutes = elapsed_time // 60
    seconds = elapsed_time % 60

    calories = round(counter * 0.5, 1)

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = pose.process(rgb_frame)

    if results.pose_landmarks:

        landmarks = results.pose_landmarks.landmark

        instruction = ""

        if exercise == "Bicep Curl":

            instruction = "Curl your arm fully"

            left_shoulder = landmarks[11]
            left_elbow = landmarks[13]
            left_wrist = landmarks[15]

            if (
                left_shoulder.visibility > 0.7 and
                left_elbow.visibility > 0.7 and
                left_wrist.visibility > 0.7
            ):

                shoulder = [
                    left_shoulder.x,
                    left_shoulder.y
                ]

                elbow = [
                    left_elbow.x,
                    left_elbow.y
                ]

                wrist = [
                    left_wrist.x,
                    left_wrist.y
                ]

                angle = calculate_angle(
                    shoulder,
                    elbow,
                    wrist
                )

                if angle > 160:
                    stage = "straight"

                elif angle < 40 and stage == "straight":
                    stage = "bent"
                    counter += 1

                h, w, c = frame.shape

                elbow_x = int(left_elbow.x * w)
                elbow_y = int(left_elbow.y * h)

                cv2.putText(
                    frame,
                    str(int(angle)),
                    (elbow_x, elbow_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

            else:

                stage = None

                cv2.putText(
                    frame,
                    "Keep your full left arm visible",
                    (20, 170),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )
        elif exercise == "Squat":

            instruction = "Keep your back straight"

            left_hip = landmarks[23]
            left_knee = landmarks[25]
            left_ankle = landmarks[27]

            hip = [left_hip.x, left_hip.y]
            knee = [left_knee.x, left_knee.y]
            ankle = [left_ankle.x, left_ankle.y]

            angle = calculate_angle(
                hip,
                knee,
                ankle
            )

            if angle < 100:
                stage = "down"

            elif angle > 160 and stage == "down":
                stage = "up"
                counter += 1

            h, w, c = frame.shape

            knee_x = int(left_knee.x * w)
            knee_y = int(left_knee.y * h)

            cv2.putText(
                frame,
                str(int(angle)),
                (knee_x, knee_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2
            )



        elif exercise == "Shoulder Press":

            instruction = "Press your hands overhead"

            left_shoulder = landmarks[11]
            left_elbow = landmarks[13]
            left_wrist = landmarks[15]

            shoulder = [
                left_shoulder.x,
                left_shoulder.y
            ]

            elbow = [
                left_elbow.x,
                left_elbow.y
            ]

            wrist = [
                left_wrist.x,
                left_wrist.y
            ]

            angle = calculate_angle(
                shoulder,
                elbow,
                wrist
            )

            if angle < 90:
                stage = "down"

            elif (
                angle > 160
                and stage == "down"
                and left_wrist.y < left_shoulder.y
            ):
                stage = "up"
                counter += 1

            h, w, c = frame.shape

            elbow_x = int(left_elbow.x * w)
            elbow_y = int(left_elbow.y * h)

            cv2.putText(
                frame,
                str(int(angle)),
                (elbow_x, elbow_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2
            )


        cv2.putText(
            frame,
            f"Reps: {counter}",
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )

        cv2.putText(
            frame,
            f"Stage: {stage}",
            (20,90),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )

        cv2.putText(
            frame,
            f"Exercise: {exercise}",
            (20,130),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,0,0),
            2
        )

        cv2.putText(
            frame,
            f"Instruction: {instruction}",
            (20,210),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )
    

        cv2.putText(
            frame,
         f"Time: {minutes:02}:{seconds:02}",
         (20, 250),
         cv2.FONT_HERSHEY_SIMPLEX,
          0.7,
         (255, 255, 0),
          2
)

        cv2.putText(
          frame,
         f"Calories: {calories} kcal",
         (20,290),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.7,
          (0,255,255),
           2
 )
        cv2.putText(
          frame,
         f"Goal: {counter}/{goal}",
        (20, 330),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.7,
         (0, 255, 0),
           2
)
        if counter >= goal:

         cv2.putText(
         frame,
        "Goal Completed!",
        (250,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        3
 )

        mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    else:

        stage = None

        cv2.putText(
            frame,
            "No Person Detected",
            (40,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )

        cv2.putText(
            frame,
            "Please stand in front of the camera",
            (40,90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,255),
            2
        )

   

    cv2.imshow(
        "AI Personal Fitness Coach",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("1"):
        exercise = "Bicep Curl"
        counter = 0
        stage = None

    elif key == ord("2"):
        exercise = "Squat"
        counter = 0
        stage = None

    elif key == ord("3"):
        exercise = "Shoulder Press"
        counter = 0
        stage = None

    elif key == ord('q'):

        total_time = int(time.time() - start_time)

        minutes = total_time // 60
        seconds = total_time % 60

        calories = round(counter * 0.5, 1)

        print("\n========== WORKOUT SUMMARY ==========")
        print("Exercise :", exercise)
        print("Total Reps :", counter)
        print(f"Duration : {minutes:02}:{seconds:02}")
        print("Calories Burned :", calories, "kcal")
        print("=====================================\n")

        file_exists = os.path.isfile("workout_history.csv")

        with open("workout_history.csv", "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:

                writer.writerow([
                    "Exercise",
                    "Reps",
                    "Duration",
                    "Calories"
                ])

            writer.writerow([
                exercise,
                counter,
                f"{minutes:02}:{seconds:02}",
                calories
            ])

        break

cap.release()
cv2.destroyAllWindows()