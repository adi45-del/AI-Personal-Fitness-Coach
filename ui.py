import streamlit as st

st.set_page_config(
    page_title="AI Personal Fitness Coach",
    page_icon="🏋️",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#4CAF50;'>
    🏋️ AI PERSONAL FITNESS COACH
    </h1>

    <h4 style='text-align:center;color:gray;'>
    Real-Time Pose Estimation | Rep Counter | AI Workout Assistant
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

left, right = st.columns([2,1])

with left:

    st.subheader("Workout Settings")

    exercise = st.selectbox(
        "🏃 Select Exercise",
        [
            "Bicep Curl",
            "Squat",
            "Shoulder Press"
        ]
    )

    goal = st.slider(
        "🎯 Goal Repetitions",
        5,
        50,
        20
    )

    mode = st.radio(
        "📹 Workout Mode",
        [
            "Live Webcam",
            "Upload Video"
        ]
    )

    uploaded_video = None

    if mode == "Upload Video":
        uploaded_video = st.file_uploader(
            "Upload Exercise Video",
            type=["mp4","avi","mov"]
        )

    start = st.button(
        "🚀 Start Workout",
        use_container_width=True
    )

with right:

    st.subheader("Live Dashboard")

    st.metric("💪 Reps","0")

    st.metric("🔥 Calories","0 kcal")

    st.metric("⏱ Time","00:00")

    st.metric("🎯 Goal",f"0/{goal}")

    st.progress(0)

st.divider()

st.subheader("✨ Features")

c1,c2,c3 = st.columns(3)

with c1:
    st.success("✅ Live Pose Detection")
    st.success("✅ Rep Counter")
    st.success("✅ Goal Tracking")

with c2:
    st.success("✅ Exercise Recognition")
    st.success("✅ Calories Estimation")
    st.success("✅ Workout Timer")

with c3:
    st.success("✅ Workout History")
    st.success("✅ Video Upload")
    st.success("✅ AI Powered")

st.divider()

st.info(
    "Developed using Python • OpenCV • MediaPipe • Streamlit"
)