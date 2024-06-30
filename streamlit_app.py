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

    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    question, correct_answer = generate_question()
    user_answer = st.text_input(question, key=f'user_answer_{st.session_state.question_index}')

    if st.button("Submit Answer"):
        if user_answer.strip().isdigit():
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                st.success("Correct! 🎉")
                st.markdown("""
                <style>
                .balloon-animation {
                    position: absolute;
                    animation: balloon 0.5s ease-out;
                    transform: translate(-50%, 0);
                    z-index: 1;
                }
                @keyframes balloon {
                    0% { transform: translateY(0); opacity: 1; }
                    50% { opacity: 1; }
                    100% { transform: translateY(-150px); opacity: 0; }
                }
                </style>
                <div class="balloon-animation">
                <img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/271/balloon_1f388.png" width="50">
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Wrong answer! 😔 Try again.")
                st.warning("The correct answer was: " + str(correct_answer))

        st.session_state.question_index += 1

    if st.session_state.question_index > 0:
        st.button("Next Question", on_click=run_quiz)

# Main function to run the app
def main():
    run_quiz()

if __name__ == "__main__":
    main()
