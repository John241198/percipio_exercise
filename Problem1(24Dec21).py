#Problem 1:
"""
Play a sample video from your local directory using VLC media player.
"""


import subprocess
vlc=r"C:\Program Files\VideoLAN\VLC\vlc.exe"
file=subprocess.Popen([vlc,r"C:\Users\ELCOT\HCL Python Training\john\Inside Man 2006.720p.BrRip.x264.YIFY.mp4"])
print("Vlc player is running!....")
#file.terminate()
quit=input("enter quit for terminate video:")
if quit=="quit":
    file.terminate()

