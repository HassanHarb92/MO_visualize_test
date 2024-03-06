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

# Layout for two columns
col1, col2 = st.columns(2)

# Dropdown menus for selecting cube files for each visualizer
with col1:
    st.write("Visualizer 1")
    selected_cube_file_name_1 = st.selectbox('Select a cube file for the first visualizer:', cube_files_names, key='1')

with col2:
    st.write("Visualizer 2")
    selected_cube_file_name_2 = st.selectbox('Select a cube file for the second visualizer:', cube_files_names, index=1, key='2')

# Visualization button
if st.button('Visualize Selected Orbitals'):
    if selected_cube_file_name_1 and selected_cube_file_name_2:
        # Full paths to the selected cube files
        selected_cube_file_path_1 = os.path.join(cubes_directory, selected_cube_file_name_1)
        selected_cube_file_path_2 = os.path.join(cubes_directory, selected_cube_file_name_2)
        
        # Visualize the selected cube files in separate columns
        with col1:
            visualize_cube(selected_cube_file_path_1, alpha)
        with col2:
            visualize_cube(selected_cube_file_path_2, alpha)

