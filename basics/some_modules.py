# ============================
# PYTHON MODULE REVISION FILE
# glob, csv, shutil, webbrowser
# ============================


# --------- 1. glob MODULE ----------
# Used to find files/folders using patterns (wildcards like *.txt)

import glob

# Finds all Python files in current directory
python_files = glob.glob("*.py")

print("Python files found:")
print(python_files)



# --------- 2. csv MODULE ----------
# Used to read and write CSV (Comma Separated Values) files

import csv

# Open a CSV file in read mode
# CSV file example:
# name,age
# Alex,20
# Bob,22

with open("sample.csv", "r") as file:
    reader = csv.reader(file)  # creates a CSV reader object

    for row in reader:
        # Each row is a list
        print(row)



# --------- 3. shutil MODULE ----------
# Used for high-level file operations like copy, move, delete

import shutil

# Copy a file from source to destination
# Syntax: shutil.copy(source, destination)

shutil.copy("sample.txt", "sample_copy.txt")

print("File copied successfully")



# --------- 4. webbrowser MODULE ----------
# Used to open websites using the default browser

import webbrowser

# Opens Python official website in browser
webbrowser.open("https://www.python.org")

print("Browser opened")