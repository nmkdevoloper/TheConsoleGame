import requests
import time
import os
import shutil
from tqdm import tqdm

# Set the console title
def set_console_title(title):
    os.system(f"title {title}")

# Create the target directory
def create_directory(path):
    os.makedirs(path, exist_ok=True)

# Download a list of files with progress display
def download_files(file_urls):
    for url, filename in file_urls:
        try:
            print(f"Downloading {filename}...")
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Check for HTTP errors

            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

            with open(filename, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()

            if total_size != 0 and progress_bar.n != total_size:
                print("Error! Something went wrong during the download.")
                time.sleep(3)
                exit()
        except requests.exceptions.RequestException as e:
            print(f"Error! Failed to download {filename}: {e}")
            time.sleep(3)
            exit()

# Move a list of files to a target directory
def move_files(file_list, target_dir):
    for filename in file_list:
        try:
            shutil.move(filename, os.path.join(target_dir, filename))
        except shutil.Error:
            print(f"Error! Cannot move {filename}. Please remove the old folder before running this installer!")
            time.sleep(3)
            exit()

# Copy a file back to the current directory
def copy_file_to_current_dir(src_path):
    try:
        shutil.copy2(src_path, ".")
    except shutil.Error:
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
        ("https://shattereddisk.github.io/rickroll/rickroll.mp4", "troll.mp4")
    ]
    download_files(file_urls)

    file_list = ["TheIndex.py", "000-Example.py", "000-Example.txt", "troll.mp4"]
    move_files(file_list, target_dir)

    copy_file_to_current_dir(os.path.join(target_dir, "TheIndex.py"))

    notify_user()

# Run the main function
if __name__ == "__main__":
    main()
