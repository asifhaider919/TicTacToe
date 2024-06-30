import streamlit as st

# Initialize the game board and players' names
if 'board' not in st.session_state:
    st.session_state.board = [' ' for _ in range(9)]
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.moves = 0
    st.session_state.player_X = ''
    st.session_state.player_O = ''

# Sidebar input for players' names
st.sidebar.title("Player Information")
st.session_state.player_X = st.sidebar.text_input("Player 1 (X)", st.session_state.player_X)
st.session_state.player_O = st.sidebar.text_input("Player 2 (O)", st.session_state.player_O)

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
    [0, 4, 8], [2, 4, 6]  # Diagonal
]

# Function to check for a winner
def check_winner():
    for combo in winning_combinations:
        if st.session_state.board[combo[0]] == st.session_state.board[combo[1]] == st.session_state.board[combo[2]] != ' ':
            st.session_state.winner = st.session_state.current_player
            return True
    return False

# Function to handle a move
def make_move(index):
    if st.session_state.board[index] == ' ' and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        st.session_state.moves += 1
        if check_winner():
            st.session_state.winner = st.session_state.current_player
            st.balloons()  # Trigger the balloons animation
        elif st.session_state.moves == 9:
            st.session_state.winner = 'Tie'
        else:
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Function to reset the game
def reset_game():
    st.session_state.board = [' ' for _ in range(9)]
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.moves = 0

# Title of the app
st.title("Tic Tac Toe")

# Display whose turn it is
if st.session_state.winner is None:
    st.subheader(f"It's {st.session_state.player_X if st.session_state.current_player == 'X' else st.session_state.player_O}'s ({st.session_state.current_player}) turn")
elif st.session_state.winner == 'Tie':
    st.subheader("It's a tie!")
else:
    winner_name = st.session_state.player_X if st.session_state.winner == 'X' else st.session_state.player_O
    st.success(f"Player {winner_name} ({st.session_state.winner}) wins!")

# Styling
button_style = """
    <style>
    .stButton > button {
        height: 100px;
        width: 100px;
        font-size: 40px;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Display the game board
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        cols[j].button(st.session_state.board[index], key=index, on_click=make_move, args=(index,))

# Reset button
st.button("Reset", on_click=reset_game)
