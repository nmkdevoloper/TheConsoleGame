import time
import os
import sys
import shutil
import cv2
from ffpyplayer.player import MediaPlayer

# Constants
VIDEO_PATH = "Data (Do not touch if you do not want to skip the level)/troll.mp4"

def play_video(video_path):
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    
    # Create a maximized window
    cv2.namedWindow("Video", cv2.WND_PROP_TOPMOST)
    cv2.setWindowProperty("Video", cv2.WND_PROP_TOPMOST, 1)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_FREERATIO)
    cv2.setWindowProperty("Video", cv2.WND_PROP_AUTOSIZE, 0)

    # Set the window size to be maximized
    screen_width = cv2.getWindowImageRect("Video")[2]
    screen_height = cv2.getWindowImageRect("Video")[3]
    cv2.resizeWindow("Video", screen_width, screen_height)

    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()

        if not grabbed:
            break

        # Resize frame to fit the window while maintaining aspect ratio
        frame = cv2.resize(frame, (screen_width, screen_height), interpolation=cv2.INTER_LINEAR)

        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame  # Synchronize audio with video

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def remove_installer(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print(f"{file_name} not found!")

def set_console_title(title):
    os.system(f"title {title}")

def copy_file_to_current_dir(src_path):
    try:
        shutil.copy2(src_path, ".")
    except Exception as e:
        print(f"Error! Unable to copy {src_path} back to the current directory: {e}")
        time.sleep(3)
        exit()

def print_to_display(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    remove_installer("TheConsoleGame-Installer.py")
    set_console_title("The Console Game")

    print_to_display("Hello there!")
    print_to_display("Welcome to The Console Game!")
    print_to_display("Press [Enter] to continue!")
    input()

    os.system('cls')
    print_to_display("In this game, you need to find the answer with the hints given!")

    while True:
        print_to_display('Type "yes" to continue or "no" to close!')
        choice = input().strip().lower()
        if choice in ['yes', 'no', 'efybvuburervc']:
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
    elif choice == 'efybvuburervc':
        play_video(VIDEO_PATH)
        print("Troll Ending :)")
        time.sleep(3)
        exit()
    else:
        exit()

if __name__ == "__main__":
    main()
