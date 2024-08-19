import urllib.request
import time
import os
import shutil

# Set the console title
def set_console_title(title):
    os.system(f"title {title}")

# Create the target directory
def create_directory(path):
    os.makedirs(path, exist_ok=True)

# Download a list of files
def download_files(file_urls):
    for url, filename in file_urls:
        try:
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, filename)
        except:
            print(f"Error! Failed to download {filename}. Please check your internet connection and permissions.")
            time.sleep(3)
            exit()

# Move a list of files to a target directory
def move_files(file_list, target_dir):
    for filename in file_list:
        try:
            shutil.move(filename, os.path.join(target_dir, filename))
        except:
            print(f"Error! Cannot move {filename}. Please remove the old folder before running this installer!")
            time.sleep(3)
            exit()

# Copy a file back to the current directory
def copy_file_to_current_dir(src_path):
    try:
        shutil.copy2(src_path, ".")
    except:
        print(f"Error! Unable to copy {src_path} back to the current directory.")
        time.sleep(3)
        exit()

# Notify the user
def notify_user():
    print('Please open the file "TheIndex.py" to continue!')
    time.sleep(3)

# Main function
def main():
    set_console_title("The Console Game - Installer")

    target_dir = "Data (Do not touch if you do not want to skip the level)"
    create_directory(target_dir)

    file_urls = [
        ("https://github.com/nmkdevoloper/TheConsoleGame/raw/main/TheIndex.py", "TheIndex.py"),
        ("https://github.com/nmkdevoloper/TheConsoleGame/raw/main/000-Example.py", "000-Example.py"),
        ("https://github.com/nmkdevoloper/TheConsoleGame/raw/main/000-Example.txt", "000-Example.txt"),
        ("https://shattereddisk.github.io/rickroll/rickroll.mp4", "extremelysupersecretvideo.mp4")
    ]
    download_files(file_urls)

    file_list = ["TheIndex.py", "000-Example.py", "000-Example.txt"], "extremelysupersecretvideo.mp4"]
    move_files(file_list, target_dir)

    copy_file_to_current_dir(os.path.join(target_dir, "TheIndex.py"))

    notify_user()

# Run the main function
if __name__ == "__main__":
    main()
