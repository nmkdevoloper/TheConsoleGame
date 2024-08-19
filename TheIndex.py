import time
import os
import sys
import urllib.request
import shutil

# Remove the installer file if it exists
def remove_installer(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print(f"{file_name} not found!")

# Set the console title
def set_console_title(title):
    os.system(f"title {title}")

# Copy a file back to the current directory
def copy_file_to_current_dir(src_path):
    try:
        shutil.copy2(src_path, ".")
    except Exception as e:
        print(f"Error! Unable to copy {src_path} back to the current directory: {e}")
        time.sleep(3)
        exit()

# Print text to display with a typewriter effect
def print_to_display(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces the print to display each character immediately
        time.sleep(delay)
    print()  # Move to the next line after the loop finishes

# Main game loop
def main():
    remove_installer("TheConsoleGame-Installer.py")
    set_console_title("The Console Game")

    print_to_display("Hello there!")
    print_to_display("Welcome to The Console Game!")
    print_to_display("Press [Enter] to continue!")
    input()
    
    os.system('cls')
    print_to_display("In this game, you need to find the answer with the hints given!")

    # Choice loop
    while True:
        print_to_display('Type "yes" to continue or "no" to close!')
        choice = input().strip().lower()
        if choice in ['yes', 'no']:
            break
        os.system('cls')

    if choice == 'yes':
        target_dir = "Data (Do not touch if you do not want to skip the level)"
        os.system('cls')
        print_to_display("Loading...")

        copy_file_to_current_dir(os.path.join(target_dir, "000-Example.py"))
        copy_file_to_current_dir(os.path.join(target_dir, "000-Example.txt"))

        os.system('cls')
        print_to_display("Loading completed!")
        print_to_display("Please open file 000-Example.py!")
        time.sleep(3)
    else:
        exit()

# Run the game
if __name__ == "__main__":
    main()
