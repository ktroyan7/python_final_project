import os
import random
import sys
import time
import subprocess

from project import get_image_files, choose_random_image, display_image


def test_get_image_files():
    # Create a temporary folder with some image files
    folder_path = './temp_folder'
    os.makedirs(folder_path, exist_ok=True)
    file_names = ['test.jpg', 'test.png', 'test.jpeg', 'test.txt']
    for name in file_names:
        file_path = os.path.join(folder_path, name)
        open(file_path, 'a').close()

    # Test the function
    expected_output = [os.path.join(folder_path, 'test.jpeg'),
                       os.path.join(folder_path, 'test.jpg'),
                       os.path.join(folder_path, 'test.png')]
    assert get_image_files(folder_path) == expected_output

    # Clean up the temporary folder
    for name in file_names:
        file_path = os.path.join(folder_path, name)
        os.remove(file_path)
    os.rmdir(folder_path)

def test_choose_random_image():
    # Test with a non-empty list of image files
    image_files = ['test1.jpg', 'test2.png', 'test3.jpeg']
    assert choose_random_image(image_files) in image_files

    # Test with an empty list of image files
    assert choose_random_image([]) is None


def test_display_image():
    #check that the function runs without raising exceptions.
    image_path = 'test.jpg'
    duration_ms = 1000
    try:
        display_image(image_path, duration_ms)
    except:
        assert False
    else:
        assert True
