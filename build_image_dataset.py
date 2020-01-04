import os
from fetch_image_urls import download, fetch_img_urls
from selenium import webdriver
def search_and_download(query ,driver_path, target_path='/IMG_DATASET' ,number_images=5):
    target_folder = os.path.join(target_path ,'_'.join(query.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        response = fetch_img_urls(query, number_images, wd=wd, interval=0.5)

    for url in response:
        download(target_folder ,url)
selenium_driver_path = ''
search_and_download('bus', driver_path = selenium_driver_path)