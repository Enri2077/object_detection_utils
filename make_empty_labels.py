#!/usr/bin/env python

from __future__ import print_function
import os
import sys
from glob import glob


def get_list(base_folder, pattern):
    return [y for x in os.walk(base_folder) for y in glob(os.path.join(x[0], pattern))]


# images_folder = os.path.expanduser("~/ds/yolo/erl4_small/background_images/")
images_folder = os.getcwd()

print("empty label files will be created for images in current folder", images_folder)

def create_empty_label_files():
    image_path_list = get_list(images_folder, pattern='*.jpg')
    if len(image_path_list) < 1:
        print("no images found in", images_folder)
        sys.exit(0)
    print("Number of images found:", len(image_path_list))
    for image_path in image_path_list:
        label_path = image_path[:-4] + ".txt"
        if image_path[-4:] == ".jpg":
            if not os.path.exists(label_path):
                open(label_path, 'a').close()
                print("created empty label file", label_path)
            else:
                print("label file already exists. doing nothing.", label_path)


if __name__ == "__main__":
    create_empty_label_files()
