# AI-Personal-Fitness-Coach
An AI-powered fitness coach using Python, OpenCV, MediaPipe, and Streamlit for real-time pose estimation and workout tracking.

# 🏋️ AI Personal Fitness Coach

An AI-powered fitness assistant that uses **Computer Vision** and **MediaPipe Pose Estimation** to monitor workouts in real time. The application detects body posture through a webcam, counts exercise repetitions, tracks workout duration, estimates calories burned, and stores workout history for future reference.

The project also includes a basic **video upload mode** through Streamlit, allowing users to analyze recorded workout videos in addition to live webcam sessions.

---

##  About the Project

This project was developed to explore the practical use of **Artificial Intelligence** and **Computer Vision** in the fitness domain.

Instead of manually counting repetitions, the application detects body landmarks using MediaPipe, calculates joint angles, and identifies exercise movements automatically. It provides live workout statistics while exercising and saves workout summaries after each session.

---

##  Features

### Live Exercise Tracking
- Real-time webcam-based exercise monitoring
- Supports multiple exercises
- Automatic repetition counting
- Exercise stage detection
- Joint angle visualization
- Live exercise instructions

### Workout Statistics
- Workout timer
- Estimated calories burned
- Goal tracking
- Workout summary after each session
- Workout history stored in CSV format

### Streamlit Interface
- Simple and user-friendly interface
- Live webcam mode
- Basic video upload support for workout analysis

---

## Supported Exercises

- Bicep Curl
- Squat
- Shoulder Press

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| OpenCV | Video Processing |
| MediaPipe | Human Pose Detection |
| NumPy | Mathematical Calculations |
| Streamlit | User Interface |
| Pandas | Workout Data Handling |

---

##  How It Works

1. Capture video through the webcam or upload a workout video.
2. Detect body landmarks using MediaPipe Pose.
3. Calculate joint angles from detected landmarks.
4. Identify exercise stages.
5. Count completed repetitions.
6. Display workout information in real time.
7. Save workout statistics after the session ends.

---

##  Project Structure

```
AI-Personal-Fitness-Coach/
│
├── pose_detection.py
├── app.py
├── requirements.txt
├── workout_history.csv
└── README.md
```

---

##  Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Personal-Fitness-Coach.git
```

Move into the project folder:

```bash
cd AI-Personal-Fitness-Coach
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python pose_detection.py
```

Or launch the Streamlit interface:

```bash
streamlit run app.py
```

---

##  Current Capabilities

✔ Live webcam workout tracking

✔ Basic uploaded video analysis

✔ Automatic repetition counting

✔ Joint angle calculation

✔ Exercise instructions

✔ Workout timer

✔ Calories estimation

✔ Goal tracking

✔ CSV workout history

---

##  Future Enhancements

Some planned improvements include:

- More accurate posture correction
- AI-based exercise feedback
- Support for additional exercises
- Personalized workout recommendations
- Progress dashboard with charts
- User authentication and profile management
- Improved uploaded video analysis

---

##  Learning Outcomes

This project helped strengthen my understanding of:

- Computer Vision
- Human Pose Estimation
- OpenCV
- MediaPipe
- Real-time Video Processing
- Python Application Development
- Streamlit UI Development

---

##  Author

**Adiba Anjum**

B.Tech – Computer Science & Engineering (AI & ML)

Interested in Artificial Intelligence, Machine Learning, Computer Vision, and Software Development.

---

##  License

This project is intended for educational and learning purposes.
