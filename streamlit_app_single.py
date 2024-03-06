import streamlit as st
import py3Dmol
import os
import glob

# Function to visualize the cube file using py3Dmol with adjustable alpha value
def visualize_cube(cube_file_path, alpha):
    width = 400
    height = 480

    viewer = py3Dmol.view(width=width, height=height)

    with open(cube_file_path, 'r') as cube_file:
        cube_data = cube_file.read()
    viewer.addModel(cube_data, "cube")

    viewer.setStyle({'stick': {}, 'sphere': {'radius': 0.5}})
    viewer.addVolumetricData(cube_data, "cube", {'isoval': 0.02, 'color': "blue", 'alpha': alpha})
    viewer.addVolumetricData(cube_data, "cube", {'isoval': -0.02, 'color': "red", 'alpha': alpha})
    viewer.zoomTo()

    viewer_html = viewer._make_html()
    st.components.v1.html(viewer_html, width=width, height=height, scrolling=False)

# Streamlit interface setup
st.title('Molecule Orbital Visualization')

# Slider for adjusting the alpha value
alpha = st.slider('Adjust the alpha value for visualization:', min_value=0.0, max_value=1.0, value=0.65, step=0.05)

# Path to the cubes directory
cubes_directory = 'cubes'

# List all .cube files in the cubes directory
cube_files = glob.glob(os.path.join(cubes_directory, '*.cube'))
cube_files_names = [os.path.basename(cube_file) for cube_file in cube_files]

# Dropdown menu for selecting cube file for the visualizer
st.write("Visualizer")
selected_cube_file_name = st.selectbox('Select a cube file for the visualizer:', cube_files_names)

# Visualization button
if st.button('Visualize Selected Orbital'):
    if selected_cube_file_name:
        # Full path to the selected cube file
        selected_cube_file_path = os.path.join(cubes_directory, selected_cube_file_name)

        # Visualize the selected cube file
        visualize_cube(selected_cube_file_path, alpha)

