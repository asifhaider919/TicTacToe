import streamlit as st
import random

# Function to generate random math questions
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '*', '/'])
    if operator == '/':
        # Ensure division result is an integer
        num1 = num2 * random.randint(1, 10)  # Make num1 a multiple of num2
    question = f"What is {num1} {operator} {num2}?"
    if operator == '/':
        answer = num1 // num2  # Integer division for division operation
    else:
        answer = eval(f"{num1} {operator} {num2}")  # Evaluate the expression
    return question, answer

# Function to initialize quiz state
def init_quiz_state():
    st.session_state.quiz_score = 0
    st.session_state.question_index = 0
    st.session_state.questions = []

# Function to run the quiz
def run_quiz():
    if 'quiz_score' not in st.session_state:
        init_quiz_state()

    st.title("Math Quiz for Year 8")
    st.markdown("Answer 10 questions to test your math skills!")

    if len(st.session_state.questions) < 10:
        # Generate questions if not already generated
        for _ in range(10 - len(st.session_state.questions)):
            question, answer = generate_question()
            st.session_state.questions.append((question, answer))

    question_index = st.session_state.question_index

    if question_index < 10:
        question, correct_answer = st.session_state.questions[question_index]
        user_answer = st.text_input(f"Question {question_index + 1}: {question}")

        if st.button("Submit Answer"):
            if user_answer.strip().isdigit():
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    st.session_state.quiz_score += 1

            st.session_state.question_index += 1

    if question_index >= 10:
        st.success(f"Quiz complete! You scored {st.session_state.quiz_score}/10.")
        st.button("Restart Quiz", on_click=restart_quiz)

def restart_quiz():
    st.session_state.quiz_score = 0
    st.session_state.question_index = 0
    st.session_state.questions = []
    run_quiz()

# Main function to run the app
def main():
    st.sidebar.title("Math Quiz Options")
    start_quiz = st.sidebar.button("Start Quiz")

    if start_quiz:
        run_quiz()

if __name__ == "__main__":
    main()
