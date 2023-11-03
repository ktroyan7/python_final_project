# python_final_project
 Final project for CS50P

#### Name: Kevin Troyan
#### Date: May 2023
#### Current Location: Playa del Carmen, Mexico
#### TITLE: Image Display Program (for motivation, workplace stress, anxiety, etc.)
#### Video Demo: https://youtu.be/0uUtXiJWrtk

### Instructions:
1. Navigate to the folder containing the python script
2. Run the script in the command line (python3 project.py) and enter the 4 command line arguments
3. argv1 is the path to the folder of images you want to use
4. argv2 is how long the program will run in seconds
5. argv3 is how long the image will flash in ms (can start with 2000ms and adjust down by 500 increments if you want it to flash quicker)
6. argv4 is the time period to wait between showing the photos in seconds.
7. e.g. command line input = python3 project.py /Users/kevintroyan/downloads/project 3600 2000 30
This will script will show photos from the project folder in my downloads folder and run for 3600 seconds (1 hour) and flash and image for 2000ms (2 seconds) and flash a photo every 30 seconds


#### Description: 

This Python program displays a series of images from a folder on the screen for a specified duration and with a specified waiting time between each image. The program selects a random image file from the folder, displays it for the specified duration, and then waits for the specified time before selecting another image to display.

Files
The program consists of a single Python file, projectpy. This file contains the following functions:

get_image_files(folder_path): This function takes a folder path as input and returns a list of all image files (i.e., files ending with ".jpg", ".png", or ".jpeg") in the folder.

choose_random_image(image_files): This function takes a list of image files as input and returns a random image file path. If there are no image files in the list, the function returns None.

display_image(image_path, duration_ms): This function takes an image file path and a duration in milliseconds as input and displays the image file using the default image viewer for the system. It then waits for the specified duration and closes the image file.

main(): This function is the main entry point for the program. It takes four command-line arguments: 
1 - the path to the folder containing the images
2 - the duration of the program in seconds
3 - the duration to display each image in milliseconds
4 - the waiting time between each image in seconds. 

The function loops until the specified duration is reached, selecting and displaying a random image file from the folder on each iteration.

Design Choices
One design choice that was made in the program was to use the subprocess module to open and close the image files. This was done because the module provides a cross-platform way to interact with system processes, allowing the program to work on different operating systems.

Another design choice was to include a check for whether there are any image files in the folder. If there are no image files, the program skips to the next iteration of the loop. This was done to prevent the program from crashing if there are no images in the folder.

Finally, the program uses the time module to handle the timing of the program. Specifically, the program uses the time.sleep() function to wait for the specified durations between each iteration of the loop. This was done to simplify the program and avoid using more complex timing mechanisms.

In conclusion, this Python program provides a simple way to display a series of images from a folder on the screen for a specified duration and with a specified waiting time between each image. The program is designed to be easy to use and cross-platform, and includes checks to prevent errors if there are no images in the folder.