import streamlit as st
import pandas as pd
import folium
from shapely.geometry import Point
import math

# Sample data (replace with your actual data loading code)
data = pd.DataFrame({
    'SITECODE': ['Site1', 'Site2'],
    'SITENAME': ['Tower A', 'Tower B'],
    'CELL': ['Cell1', 'Cell2'],
    'LATITUDE': [51.5074, 52.3792],     # Sample latitudes
    'LONGITUDE': [-0.1278, 4.8994],    # Sample longitudes
    'BEAMWIDTH': [60, 90],              # Sample beamwidths in degrees
    'SECTOR_SIZE': [100, 150]           # Sample sector sizes in meters
})

# Function to calculate fan shape points
def calculate_fan_points(lat, lon, beamwidth, sector_size):
    fan_points = []
    fan_radius = sector_size / 2.0  # Radius of the fan in meters

    # Calculate fan points based on beamwidth
    fan_points.append((lat, lon))  # Center of the fan
    
    num_points = 30  # Number of points to approximate the fan shape
    angle_step = math.radians(beamwidth / num_points)

    for i in range(num_points + 1):
        angle = angle_step * i
        x = lat + fan_radius * math.cos(angle)
        y = lon + fan_radius * math.sin(angle)
        fan_points.append((x, y))

    fan_points.append((lat, lon))  # Close the polygon

    return fan_points

# Function to plot cells on the map
def plot_cells_on_map(df):
    # Create a map centered around the mean location of all data points
    m = folium.Map(location=[df['LATITUDE'].mean(), df['LONGITUDE'].mean()], zoom_start=10)

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Calculate fan shape points
        fan_points = calculate_fan_points(row['LATITUDE'], row['LONGITUDE'], row['BEAMWIDTH'], row['SECTOR_SIZE'])
        
        # Create a polygon from fan points
        polygon = folium.Polygon(locations=fan_points, color='blue', fill=True, fill_color='blue', fill_opacity=0.4)
        
        # Add popup with site and cell information
        popup = folium.Popup(f"Site: {row['SITECODE']} - {row['SITENAME']}<br>Cell: {row['CELL']}<br>Beamwidth: {row['BEAMWIDTH']}°<br>Sector Size: {row['SECTOR_SIZE']} meters")
        polygon.add_child(popup)
        
        # Add polygon to the map
        polygon.add_to(m)
    
    # Display the map
    folium_static(m, width=900, height=700)

# Main function to run the app
def main():
    st.title("Telecom Tower Cell Visualization")
    st.markdown("Visualizing telecom tower cells as fan-shaped polygons on a map.")

    # Display the cells on the map
    plot_cells_on_map(data)

if __name__ == "__main__":
    main()
