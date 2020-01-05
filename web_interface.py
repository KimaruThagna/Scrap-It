import streamlit as st
from build_image_dataset import search_and_download, selenium_driver_path
st.header("DATASET BUILDER")
st.write('Using the below interface, You can now scrap the web to obtain images and build a dataset of choice')
query = st.text_input('Enter the Query text')
max_size = st.number_input('Max number of images')

# perform dataset download
if query and max_size != 0.00:
    st.write('Downloading...')
    search_and_download(query, driver_path = selenium_driver_path, target_path='IMG_DATASET',number_images=max_size)
    st.write(f'Download complete! Check the IMG_DATASET folder')
