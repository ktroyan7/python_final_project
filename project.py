import os
import random
import sys
import time
import subprocess

"""Get a list of all image files in the specified folder"""
def get_image_files(folder_path):
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                   if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]
    return image_files

"""Choose a random image file from the list"""
def choose_random_image(image_files):
    # If there are no image files in the folder, return None
    if not image_files:
        return None
    # Return a random image file path
    return random.choice(image_files)

"""Display the specified image file for the given duration"""
def display_image(image_path, duration_ms):
    # Open the image file using the default image viewer
    subprocess.run(["open", image_path])
    # Wait for the specified duration in milliseconds
    time.sleep(duration_ms / 1000)
    # Close the image file
    subprocess.run(["osascript", "-e", 'tell application "Preview" to close document 1'])

"""The main entry point for the program"""
def main():
    # Get the command line arguments
    folder_path = sys.argv[1]
    duration_sec = int(sys.argv[2])
    flash_duration_ms = int(sys.argv[3])
    wait_time_sec = int(sys.argv[4])

    # Loop until the specified duration is reached
    start_time = time.time()
    while time.time() - start_time < duration_sec:
        # Get a list of all image files in the specified folder
        image_files = get_image_files(folder_path)
        # Choose a random image file from the list
        image_path = choose_random_image(image_files)
        # If there are no image files in the folder, skip to the next iteration of the loop
        if image_path is None:
            continue
        # Display the image for the specified duration
        display_image(image_path, flash_duration_ms)
        # Wait for the specified time before selecting another image
        time.sleep(wait_time_sec)

if __name__ == '__main__':
    main()

