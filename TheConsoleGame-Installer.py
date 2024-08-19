import urllib.request
import time
from os import system
system("title " + "The Console Game - Installer")

print("Downloading...")
urllib.request.urlretrieve("https://github.com/nmkdevoloper/TheConsoleGame/raw/main/TheIndex.py", "TheIndex.py")
print("Please open file ""TheIndex.py"" to continue!")
time.sleep(3)