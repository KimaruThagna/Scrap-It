import os
from fetch_image_urls import download, fetch_img_urls
from selenium import webdriver
def search_and_download(query ,driver_path, target_path='./images' ,number_images=5):
    target_folder = os.path.join(target_path ,'_'.join(query.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_img_urls(query, number_images, wd=wd, interval=0.5)

    for elem in res:
        download(target_folder ,elem)