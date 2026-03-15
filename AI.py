import streamlit as st
import requests

API_URL = "http://localhost:5000"

st.title("Ultimate AI Student Mentor & Debate Coach")

user_id = st.text_input("Enter your user ID:")

menu = ["Study Plan","Homework Help","Mini Quiz","Debate","Proactive Question","Code Generator","Code Debugger","Research Assistance","Project Ideas","History"]
choice = st.sidebar.selectbox("Select Feature", menu)

if choice == "Study Plan":
    subjects = st.text_input("Subjects (comma-separated)")
    exam_dates = st.text_input("Exam Dates (comma-separated)")
    hours_per_day = st.number_input("Hours per day", 1, 12, 2)
    if st.button("Generate Study Plan"):
        data = {"user_id": user_id, "subjects": subjects, "exam_dates": exam_dates, "hours_per_day": hours_per_day}
        res = requests.post(f"{API_URL}/study_plan", json=data).json()
        st.text_area("AI Study Plan", res["response"], height=300)

elif choice == "Homework Help":
    question = st.text_area("Enter your homework question")
    notes_text = st.text_area("Optional notes / textbook reference")
    if st.button("Get Help"):
        data = {"user_id": user_id, "question": question, "notes_text": notes_text}
        res = requests.post(f"{API_URL}/homework", json=data).json()
        st.text_area("AI Explanation", res["response"], height=300)

elif choice == "Mini Quiz":
    topic = st.text_input("Topic for quiz")
    notes_text = st.text_area("Optional notes / textbook reference")
    if st.button("Generate Quiz"):
        data = {"user_id": user_id, "topic": topic, "notes_text": notes_text}
        res = requests.post(f"{API_URL}/quiz", json=data).json()
        st.text_area("AI Quiz", res["response"], height=300)

elif choice == "Debate":
    argument = st.text_area("Enter your argument / statement")
    notes_text = st.text_area("Optional notes / textbook reference")
    if st.button("Start Debate"):
        data = {"user_id": user_id, "student_argument": argument, "notes_text": notes_text}
        res = requests.post(f"{API_URL}/debate", json=data).json()
        st.text_area("AI Debate Response", res["response"], height=300)

elif choice == "Proactive Question":
    if st.button("Generate Question"):
        data = {"user_id": user_id}
        res = requests.post(f"{API_URL}/proactive_question", json=data).json()
        st.text_area("AI Proactive Question", res["response"], height=150)

elif choice == "Code Generator":
    task = st.text_area("Describe the coding task")
    language = st.text_input("Programming language", "Python")
    if st.button("Generate Code"):
        data = {"user_id": user_id, "task": task, "language": language}
        res = requests.post(f"{API_URL}/code_generate", json=data).json()
        st.text_area("AI Generated Code", res["response"], height=300)

elif choice == "Code Debugger":
    code = st.text_area("Paste your code here")
    language = st.text_input("Programming language", "Python")
    if st.button("Debug Code"):
        data = {"user_id": user_id, "code": code, "language": language}
        res = requests.post(f"{API_URL}/code_debug", json=data).json()
        st.text_area("AI Debugger Response", res["response"], height=300)

elif choice == "Research Assistance":
    topic = st.text_area("Enter topic to research")
    if st.button("Get Summary"):
        data = {"user_id": user_id, "topic": topic}
        res = requests.post(f"{API_URL}/research", json=data).json()
        st.text_area("Research Summary & References", res["response"], height=300)

elif choice == "Project Ideas":
    subject = st.text_input("Subject / Field")
    level = st.text_input("Student Level (high school/college)", "college")
    if st.button("Generate Project Ideas"):
        data = {"user_id": user_id, "subject": subject, "level": level}
        res = requests.post(f"{API_URL}/project_ideas", json=data).json()
        st.text_area("AI Project Ideas", res["response"], height=300)

elif choice == "History":
    res = requests.get(f"{API_URL}/history/{user_id}").json()
    for h in res:
        st.write(f"{h['type']}: {h['response']}")
