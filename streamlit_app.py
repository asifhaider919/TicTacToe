import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data for Gantt chart
data = pd.DataFrame({
    'Task': ['Task 1', 'Task 2', 'Task 3', 'Task 4'],
    'Start': pd.to_datetime(['2024-07-01', '2024-07-05', '2024-07-08', '2024-07-10']),
    'Finish': pd.to_datetime(['2024-07-10', '2024-07-15', '2024-07-18', '2024-07-20'])
})

# Function to create Gantt chart
def create_gantt_chart(df):
    fig = px.timeline(df, x_start='Start', x_end='Finish', y='Task', title='Sample Gantt Chart')
    fig.update_layout(xaxis_title='Timeline', yaxis_title='Tasks')
    return fig

# Main function to run the app
def main():
    st.title('Sample Gantt Chart')
    st.markdown('Here is a sample Gantt chart created using Plotly.')

    # Display the Gantt chart
    st.plotly_chart(create_gantt_chart(data))

if __name__ == '__main__':
    main()
