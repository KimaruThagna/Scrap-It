import time, io, requests, hashlib, os
from PIL import Image

def fetch_img_urls(query, max_links_to_fetch, wd, interval):
    def scroll_to_end(wd): # simulate scrolling action to the bottom of page
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(interval)
    # build the google query.
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    # load the page with query
    wd.get(search_url.format(q=query))
    img_urls, img_count, results_start = set(), 0, 0
    while img_count < max_links_to_fetch: # go on unless max number is attained
        scroll_to_end(wd) # to load all images
        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.rg_ic")
        result_count = len(thumbnail_results)

        print(f"Found: {result_count} search results. Extracting links from {results_start}:{result_count}")

        for img in thumbnail_results[results_start:result_count]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(interval)
            except Exception:
                continue
            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.irc_mi')
            for actual_image in actual_images:
                if actual_image.get_attribute('src'): # if image has an src attribute
                    img_urls.add(actual_image.get_attribute('src'))# add to set

            img_count = len(img_urls)

            if len(img_urls) >= max_links_to_fetch:
                print(f"Found: {len(img_urls)} image links, done!")
                break
            else:
                print("Found:", len(img_urls), "image links, looking for more ...")
                time.sleep(1)
                load_more_button = wd.find_element_by_css_selector(".ksb")
                if load_more_button:
                    wd.execute_script("document.querySelector('.ksb').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return img_urls

def download(folder_path,url):
    image_content = ""
    try:
        image_content = requests.get(url).content # image url from src parameter

    except Exception as e:
        print(f"ERROR - Could not download the image{url} -  due to {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        # perform a hex digest of image and pick first 10 chars for image name
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as image in {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")