import folium

# Create a map centered at a specific location
m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)  # London, UK coordinates

# Add a marker with a popup
folium.Marker(
    location=[51.509865, -0.118092],  # Coordinates for Big Ben
    popup='Big Ben',
    icon=folium.Icon(color='blue')
).add_to(m)

# Add another marker with a different icon
folium.Marker(
    location=[51.5007, -0.1246],  # Coordinates for the London Eye
    popup='London Eye',
    icon=folium.Icon(color='green', icon='cloud')
).add_to(m)

# Save the map as an HTML file
m.save('simple_map.html')

# Open the map in a web browser
import webbrowser
webbrowser.open('simple_map.html')
