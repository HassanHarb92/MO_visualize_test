import streamlit as st
import py3Dmol
import os

# Function to visualize the molecule and the orbital from cube files using py3Dmol
def visualize_cube(molecule_cube_file_path, orbital_cube_file_path):
    width = 640
    height = 480

    # Initialize the viewer with specified width and height
    viewer = py3Dmol.view(width=width, height=height)
    
    # Add the molecule from the cube file
    with open(molecule_cube_file_path, 'r') as molecule_file:
        molecule_data = molecule_file.read()
    viewer.addModel(molecule_data, "cube")
    
    # Add the molecular orbital from another cube file
    # If the orbital data is in the same cube file, this step can be adjusted or skipped
    with open(orbital_cube_file_path, 'r') as orbital_file:
        orbital_data = orbital_file.read()
    viewer.addModel(orbital_data, "cube")
    
    # Set the visualization style and zoom to fit
    viewer.setStyle({'stick': {}})
    viewer.addVolumetricData(orbital_data, "cube", {'isoval': 0.02, 'color': "blue", 'alpha': 0.65})
    viewer.addVolumetricData(orbital_data, "cube", {'isoval': -0.02, 'color': "red", 'alpha': 0.65})
    viewer.zoomTo()
    
    # Render the viewer to HTML and embed it in Streamlit using components
    viewer_html = viewer._make_html()
    st.components.v1.html(viewer_html, width=width, height=height, scrolling=False)

# Streamlit interface
st.title('Molecule and Orbital Visualization')

# Assuming the cube files are located in the same directory as your Streamlit app
molecule_cube_file_path = 'H2-sto3g.cube'  
orbital_cube_file_path = 'H2-sto3g.cube'  

if st.button('Visualize'):
    # Visualize the molecule and the orbital
    visualize_cube(molecule_cube_file_path, orbital_cube_file_path)

