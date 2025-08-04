from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import keyboard
import pyautogui
import ctypes
import os


# Initialize the audio endpoint volume interface
device = AudioUtilities.GetSpeakers()
interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# Cast to the IAudioEndpointVolume interface
volume_ctrl = cast(interface, POINTER(IAudioEndpointVolume))

def get_system_volume():
    # Get the current volume level (0.0 to 1.0)
    return volume_ctrl.GetMasterVolumeLevelScalar()

# Set volume (range is from 0.0 to 1.0)
def set_system_volume(level):
    level = max(0.0, min(1.0, level))  # make sure level is between 0.0 and 1.0
    volume_ctrl.SetMasterVolumeLevelScalar(level, None) # Set the system volume
    
def toggle_play_pause():
    keyboard.send("play/pause media")

def update_song(direction):
    if direction == "next":
        print("Next song")
        # pyautogui.hotkey('ctrl', 'f')
        pyautogui.press("l")
        # ctypes.windll.user32.keybd_event(0xB0, 0, 0, 0)

    elif direction == "previous":
        print("Previous song")
        # pyautogui.hotkey('ctrl', 'b')
        pyautogui.press("j")
        # ctypes.windll.user32.keybd_event(0xB1, 0, 0, 0)