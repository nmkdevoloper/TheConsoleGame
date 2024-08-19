import time
import os
import sys

# Remove TheIndex.py if it exists
def remove_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print(f"{file_name} not found!")

# Set the console title
def set_console_title(title):
    os.system(f"title {title}")

# Print text to display with a typewriter effect
def print_to_display(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Main game logic
def main():
    remove_file("TheIndex.py")
    set_console_title("The Console Game - 000. Example")

    print_to_display('Welcome back! Can you see the "000-Example.txt"?')
    print_to_display("Open this file and type the answer here!")

    # Loop until the correct answer is given
    while input().strip() != "1234":
        os.system('cls')
        print_to_display("Wrong answer, try again!")

    os.system('cls')
    print_to_display("Good job! You passed this level!")
    print_to_display("Loading...")

# Run the game
if __name__ == "__main__":
    main()
