import streamlit as st
from build_image_dataset import search_and_download, selenium_driver_path
st.header("DATASET BUILDER")
st.write('Using the below interface, You can now scrap the web to obtain images and build a dataset of choice')
query = st.text_input('Enter the Query text')
max_size = st.number_input('Max number of images')
path = st.text_input('Provide target download path. Default is IMG_DATASET')
# perform dataset download
if path is None:
    path = 'IMG_DATASET'
search_and_download(query, driver_path = selenium_driver_path, target_path=path)
if path: # if unique path was provided
    st.write(f'Download complete! Check the {path} folder')
else:
    st.write(f'Download complete! Check the IMG_DATASET folder')
#
# # user may want to see a sample image
# if st.checkbox('Show sample Image from downloaded dataset'):
#     img = ''
#     st.image(img,caption='Sample image' )