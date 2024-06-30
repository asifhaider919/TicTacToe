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

# Function to run the quiz
def run_quiz():
    st.title("Math Quiz for Year 8")
    st.markdown("Answer 10 questions to test your math skills!")

    score = 0
    for i in range(10):
        question, correct_answer = generate_question()
        user_answer = st.text_input(f"Question {i + 1}: {question}")
        if user_answer.strip().isdigit():  # Check if the input is a number
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                score += 1

    st.success(f"You scored {score}/10!")

# Main function to run the app
def main():
    st.sidebar.title("Math Quiz Options")
    start_quiz = st.sidebar.button("Start Quiz")

    if start_quiz:
        run_quiz()

if __name__ == "__main__":
    main()
