import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6K-fgXC7Hf4Bj2-ZUF0Pej4sD0LAYSgtopYd5R5Bp9zUw")

model = genai.GenerativeModel("gemini-2.5-flash")

# 🎨 App UI
st.set_page_config(page_title="Bindusree AI – Python Learning Buddy", page_icon="🤖")

st.title("🤖 Bindusree AI – Python Learning Buddy")

# User Inputs
level = st.selectbox(
    "Select Your Python Level",
    ["Beginner", "Intermediate", "Advanced"]
)

topic = st.text_input("Enter Python Topic (e.g., Loops, Functions)")

# Generate Lesson
if st.button("Start Learning"):
    if topic == "":
        st.warning("Please enter a topic!")
    else:
        prompt = f"""
You are Bindusree AI – a friendly Python mentor.

Student Level: {level}
Topic: {topic}

Teach using this structure:

1. Introduction
2. Simple Explanation
3. Why It Is Important
4. Syntax
5. Real-Life Example
6. Python Code Example
7. Expected Output
8. Common Beginner Mistakes
9. Practice Question
10. Multiple Choice Quiz (5 questions, no answers)

Keep it beginner-friendly and structured.
"""

        response = model.generate_content(prompt)
        st.markdown(response.text)

# Quiz Evaluation Section
st.subheader("📝 Submit Quiz Answers")

answers = st.text_input("Enter your answers (e.g., 1-A,2-B,3-C...)")

if st.button("Evaluate Answers"):
    if answers == "" or topic == "":
        st.warning("Please enter both topic and answers!")
    else:
        eval_prompt = f"""
You are Bindusree AI.

Topic: {topic}
Student Answers: {answers}

Evaluate the answers:
- Give score out of 5
- Show correct answers
- Explain each answer
- Encourage the student
- Suggest what to revise
- Give lesson summary
- Suggest next topic
- Add motivation

Do NOT skip explanations.
"""

        result = model.generate_content(eval_prompt)
        st.markdown(result.text)
