import time

def fetch_image_urls(query, max_links_to_fetch, wd, interval):
    def scroll_to_end(wd): # simulate scrolling action to the bottom of page
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(interval)
    # build the google query.
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    # load the page with query
    wd.get(search_url.format(q=query))
    img_urls, img_count, results_start = set(), 0, 0

