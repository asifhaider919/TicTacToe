import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Step 1: Read CSV into Pandas DataFrame
file_path = 'path_to_your_file.csv'  # Replace with your file path
df = pd.read_csv(file_path, sep=';')

# Step 2: Convert 'PERIOD_START_TIME' to datetime and set as index
df['PERIOD_START_TIME'] = pd.to_datetime(df['PERIOD_START_TIME'])
df.set_index('PERIOD_START_TIME', inplace=True)

# Step 3: Calculate delta between last 'PERIOD_START_TIME' and same time last week
last_period = df.index.max()
last_week = last_period - timedelta(days=7)

df_last = df[df.index == last_period]
df_last_week = df[df.index == last_week]

# Calculate delta for dynamically selected metrics (replace 'Metric1', 'Metric2' with actual metric names)
selected_metrics = ['Metric1', 'Metric2']  # Replace with your selected metrics
delta_threshold = 10  # Example threshold, replace with your dynamic threshold

delta_items = {}
for metric in selected_metrics:
    delta = df_last[metric] - df_last_week[metric]
    delta_items[metric] = delta[delta > delta_threshold].index.tolist()

# Step 4: Prepare data for plotting
plot_data = []
for metric, items in delta_items.items():
    for item in items:
        plot_data.append({'PERIOD_START_TIME': item, 'Metric': metric, 'Value': df.loc[item, metric]})

plot_df = pd.DataFrame(plot_data)

# Step 5: Plot using Plotly Express
fig = px.line(plot_df, x='PERIOD_START_TIME', y='Value', color='Metric', title='Metrics Above Threshold')
fig.update_xaxes(title='PERIOD_START_TIME')
fig.update_yaxes(title='Metric Value')
fig.show()
