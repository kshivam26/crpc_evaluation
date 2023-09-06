import os
import re
import shutil

def create_version_folders():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all files in the current directory
    files = os.listdir(current_directory)

    # Regular expression to extract the version number from file names
    pattern = r"v(\d+)_stats.*\.txt$"

    # Create version folders and move files into them
    for filename in files:
        match = re.match(pattern, filename)
        if match:
            version_number = match.group(1)
            version_folder = f"v{version_number}_stats"
            
            if not os.path.exists(version_folder):
                os.makedirs(version_folder)

            # Move the file to the version folder
            shutil.move(filename, os.path.join(version_folder, filename))
        else:
            print("current filename: ", filename)

if __name__ == "__main__":
    create_version_folders()
