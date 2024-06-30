import pandas as pd
import datetime as dt

# Load your CSV data (adjust the path and delimiter if needed)
csv_file = 'path_to_your_csv_file.csv'
delimiter = ';'
df = pd.read_csv(csv_file, delimiter=delimiter)

# Assume Period start time is in 'PERIOD_START_TIME' column
df['PERIOD_START_TIME'] = pd.to_datetime(df['PERIOD_START_TIME'])

# Filter and select metrics dynamically (adjust as per your UI logic)
selected_metrics = ['Metric_A', 'Metric_B']  # Example: dynamically selected metrics

# Calculate the delta for each selected metric
for metric in selected_metrics:
    # Calculate delta between last 'Period start time' and last week's same day 'Period start time'
    last_period_time = df['PERIOD_START_TIME'].max()
    last_week_period_time = last_period_time - dt.timedelta(days=7)
    
    # Filter data for the last 'Period start time' and last week's same day
    last_period_data = df[df['PERIOD_START_TIME'] == last_period_time]
    last_week_data = df[df['PERIOD_START_TIME'] == last_week_period_time]
    
    # Calculate delta for the selected metric
    delta_column = f'{metric}_delta'
    df[delta_column] = last_period_data[metric] - last_week_data[metric]

# Define your dynamically set threshold
threshold = 10  # Example: dynamically set threshold

# Filter items where delta of selected metrics is above threshold
filtered_items = df[(df[selected_metrics].max(axis=1) > threshold)]

# Display on map (example using Folium)
import folium

# Create a base map centered around a location (adjust center coordinates as needed)
m = folium.Map(location=[df['Lat'].mean(), df['Lon'].mean()], zoom_start=7)

# Iterate over filtered items to plot on the map
for idx, row in filtered_items.iterrows():
    popup_message = f"<b>Item:</b> {row['Item']}<br>" \
                    f"<b>Lat:</b> {row['Lat']}<br>" \
                    f"<b>Lon:</b> {row['Lon']}<br>" \
                    f"<b>Metrics:</b><br>"
                    
    for metric in selected_metrics:
        popup_message += f"{metric}: {row[metric]}<br>"
        
    folium.Marker(
        location=[row['Lat'], row['Lon']],
        popup=folium.Popup(popup_message, max_width=400),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Display the map
folium_static(m)
