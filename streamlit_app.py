import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import math

# Function to calculate fan shape points
def calculate_fan_points(lat, lon, azimuth, beamwidth_deg, sector_size_m):
    fan_points = []
    fan_radius = sector_size_m/1000  # Sector size directly represents the radius in meters

    # Convert azimuth to radians
    azimuth_rad = math.radians(azimuth)

    # Calculate fan points based on beamwidth and azimuth
    fan_points.append((lat, lon))  # Center of the fan
    
    num_points = 30  # Number of points to approximate the fan shape
    angle_step = math.radians(beamwidth_deg / 2.0 / num_points)  # Half of the beamwidth
    
    # Calculate fan points in one direction
    for i in range(num_points + 1):
        angle = angle_step * i
        x = fan_radius * math.cos(angle)
        y = fan_radius * math.sin(angle)
        # Rotate the fan points based on azimuth
        rotated_x = x * math.cos(azimuth_rad) - y * math.sin(azimuth_rad)
        rotated_y = x * math.sin(azimuth_rad) + y * math.cos(azimuth_rad)
        fan_points.append((lat + rotated_x, lon + rotated_y))
    
    # Mirror points to the other side
    mirrored_points = [(lat, lon)] + [(2 * lat - x, 2 * lon - y) for x, y in reversed(fan_points)]
    
    return mirrored_points

# Function to plot cells on the map
def plot_cells_on_map(df):
    # Create a map centered around the mean location of all data points
    m = folium.Map(location=[df['LATITUDE'].mean(), df['LONGITUDE'].mean()], zoom_start=10)

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Calculate fan shape points
        fan_points = calculate_fan_points(row['LATITUDE'], row['LONGITUDE'], row['AZIMUTH'], row['BEAMWIDTH'], row['SECTOR_SIZE'])
        
        # Create a polygon from fan points
        polygon = folium.Polygon(locations=fan_points, color='blue', fill=True, fill_color='blue', fill_opacity=0.4)
        
        # Add popup with site and cell information
        popup = folium.Popup(f"Site: {row['SITECODE']} - {row['SITENAME']}<br>Cell: {row['CELL']}<br>Beamwidth: {row['BEAMWIDTH']}°<br>Sector Size: {row['SECTOR_SIZE']} meters")
        polygon.add_child(popup)
        
        # Add polygon to the map
        polygon.add_to(m)
    
    # Display the map
    folium_static(m)

# Main function to run the app
def main():
    st.title("Telecom Tower Cell Visualization")
    st.markdown("Visualizing telecom tower cells as fan-shaped polygons on a map.")

    # File upload
    st.sidebar.header("Upload Excel File")
    uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Read data from uploaded file
        try:
            df = pd.read_excel(uploaded_file)
            
            # Display the cells on the map
            plot_cells_on_map(df)
            
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
    
    # If no file uploaded, show instructions
    if uploaded_file is None:
        st.sidebar.info('Upload an Excel file to start')

if __name__ == "__main__":
    main()
