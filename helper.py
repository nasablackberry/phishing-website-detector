from html2image import Html2Image
import pandas as pd
import pickle
import re
import os


screenshot_dir = 'screenshot/'
stats_params = ('visits', 'checked', 'phished')

h2i = Html2Image()
h2i.output_path = screenshot_dir


stats_filename = 'stats.txt'
model = pickle.load(open("model.pkl", "rb"))


def format_url(url):
    url = url.strip()
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

