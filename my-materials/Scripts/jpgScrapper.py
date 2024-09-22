import wget
import re
import os
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="A script to download .jpg files from URLs listed in a text file.")
parser.add_argument('-f', '--file', required=True, help="Path to the file containing URLs.")
args = parser.parse_args()

# Get the file path from the parsed arguments
file_path = args.file

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
    exit()

# Open the file and read all lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Regular expression to find URLs starting with http and ending with .jpg
url_pattern = re.compile(r'(http\S+/)([^/]+)/([^/]+\.jpg)')

# Loop through each line and find valid URLs
for line in lines:
    match = url_pattern.search(line)
    if match:
        base_url = match.group(1)  # Base URL (e.g., http://team.thm/images/)
        directory = match.group(2)  # Directory (e.g., thumbs or fulls)
        filename = match.group(3)  # Original file name (e.g., 05.jpg)

        # Create new file name by prepending directory name
        new_filename = f"{directory}{filename}"

        # Full URL of the image
        full_url = base_url + directory + '/' + filename

        # Download the file with the new name
        print(f"Downloading: {full_url} as {new_filename}")
        wget.download(full_url, new_filename)

print("\nAll downloads complete!")
