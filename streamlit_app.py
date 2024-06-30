import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static  # Import folium_static from streamlit_folium

# Function to plot cells on the map
def plot_cells_on_map(df):
    # Create a map centered around the mean location of all data points
    m = folium.Map(location=[df['LATITUDE'].mean(), df['LONGITUDE'].mean()], zoom_start=10)

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Calculate fan shape points (replace with your logic)
        fan_points = [(row['LATITUDE'] + 0.1, row['LONGITUDE']),
                      (row['LATITUDE'], row['LONGITUDE'] + 0.1),
                      (row['LATITUDE'] - 0.1, row['LONGITUDE'])]

        # Create a polygon from fan points
        polygon = folium.Polygon(locations=fan_points, color='blue', fill=True, fill_color='blue', fill_opacity=0.4)
        popup = folium.Popup(f"Site: {row['SITECODE']} - {row['SITENAME']}<br>Cell: {row['CELL']}")
        polygon.add_child(popup)
        polygon.add_to(m)

    # Display the map using folium_static
    folium_static(m)

# Main function to run the app
def main():
    st.title("Telecom Tower Cell Visualization")
    st.markdown("Visualizing telecom tower cells as fan-shaped polygons on a map.")

    # Example DataFrame (replace with your actual data loading code)
    data = pd.DataFrame({
        'SITECODE': ['Site1', 'Site2'],
        'SITENAME': ['Tower A', 'Tower B'],
        'CELL': ['Cell1', 'Cell2'],
        'LATITUDE': [51.5074, 52.3792],     # Sample latitudes
        'LONGITUDE': [-0.1278, 4.8994]     # Sample longitudes
    })

    # Display the cells on the map
    plot_cells_on_map(data)

if __name__ == "__main__":
    main()
