import streamlit as st
import random

# Function to generate a random math question
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
    st.markdown("Answer each question to test your math skills!")

    question, correct_answer = generate_question()
    user_answer = st.text_input("Question:", key='user_answer')

    if st.button("Submit Answer"):
        if user_answer.strip().isdigit():
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                st.success("Correct! 🎉")
                st.balloons()
            else:
                st.error("Wrong answer! 😔 Try again.")
                st.warning("The correct answer was: " + str(correct_answer))

        st.button("Next Question", on_click=run_quiz, key='next_button')

# Main function to run the app
def main():
    run_quiz()

if __name__ == "__main__":
    main()
