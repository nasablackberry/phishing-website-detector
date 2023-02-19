from flask import send_from_directory
from html2image import Html2Image
from urllib.parse import urlparse
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


def capture_screenshot(target_url, filename='screenshot.png', size=(1920, 1080)):
    h2i.screenshot(url=target_url, save_as=filename, size=size)
    return send_from_directory(screenshot_dir, path=filename)


def get_stats(key=None):
    stats = {}
    if os.path.exists(stats_filename):
        with open(stats_filename, "r") as file:
            for line in file:
                (k, v) = line.split(":")
                stats[k] = int(v)

        if key is not None:
            return stats[key] if key in stats else None

        return stats

    return False


def update_stats(key):
    stats = get_stats()
    with open("stats.txt", "w+") as file:
        if stats is False:
            file.write('\n'.join([f"{x}:0" for x in stats_params]))
        else:
            lines = []
            avail_params = list(stats_params)
            for k, v in stats.items():
                avail_params.remove(k)
                if k == key:
                    v += 1
                lines.append(f"{k}:{v}")
            if len(avail_params) > 0:
                for param in avail_params:
                    lines.append(f"{param}:0")
            file.write("\n".join(lines))
        file.flush()
