import win32gui
import keyboard
import time
import pyautogui
import d3dshot
from PIL import Image

target_size = (640, 480)
target_location = (0, 0)
screen_grab_location_offset = (9, 34)
screen_grab_size_offset = (-9, -7)
default_region = (9, 34, 631, 473)


def window_enumeration_handler(hwnd, top_windows):
    found_object = {'app': (hwnd, win32gui.GetWindowText(hwnd))}
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    found_object['location'] = (x, y)
    found_object['size'] = (w, h)
    top_windows.append(found_object)


class Win10MinecraftApp:
    def __init__(self):
        self.d = d3dshot.create(frame_buffer_size=100, capture_output="numpy")
        self.d.capture(region=default_region)


    def move_mc(self):
        self.top_windows = []
        self.minecraft = []
        win32gui.EnumWindows(window_enumeration_handler, self.top_windows)
        for i in self.top_windows:
            if "minecraft" == i['app'][1].lower():
                self.minecraft = i
                break

        if not self.minecraft:
            lol = 1
            # raise Exception("Windows 10 Minecraft found to not be running,"
            # "Make sure Windows 10 Minecraft is running and "
            # "your world is loaded")

        win32gui.MoveWindow(self.minecraft['app'][0], target_location[0], target_location[1],
                            target_size[0], target_size[1], True)
        x0, y0, x1, y1 = win32gui.GetWindowRect(self.minecraft['app'][0])
        w = x1 - x0  # width
        h = y1 - y0  # height
        self.minecraft['location'] = (x0, y0)
        self.minecraft['size'] = (w, h)
        win32gui.SetForegroundWindow(self.minecraft['app'][0])
        region = (
            self.minecraft['location'][0] + screen_grab_location_offset[0],
            self.minecraft['location'][1] + screen_grab_location_offset[1],
            self.minecraft['size'][0] + screen_grab_size_offset[0],
            self.minecraft['size'][1] + screen_grab_size_offset[1])
        print(region)
        #self.d.capture( region=region)

        print(f"Minecraft Windows 10 Found, Loc:{self.minecraft['size']}")


    def send_keystroke(self, key_instructions):
        if not isinstance(key_instructions, list):
            raise Exception(f"Expected list of keystroke actions, got {type(key_instructions)}")

        for key_instruction in key_instructions:
            if key_instruction['action'] == 'press':
                keyboard.press(key_instruction['key'])
            elif key_instruction['action'] == 'press_and_release':
                keyboard.press(key_instruction['key'])
                time.sleep(0.1)
                keyboard.release(key_instruction['key'])
            elif key_instruction['action'] == 'release':
                keyboard.release(key_instruction['key'])
            else:
                raise Exception("Invalid Instruction to act upon")

    def is_pressed(self, key):
        return keyboard.is_pressed(key)

    def get_screen(self):
        return self.d.get_latest_frame()

    def get_screen(self, frame_count):
        if len(self.d.frame_buffer) > frame_count:
            return self.d.get_frame_stack(tuple(range(0, frame_count)), stack_dimension="last")
        else:
            return None

    def get_screen_and_keys(self):
        return self.get_screen(), self.get_keys()

    def get_screen_and_keys(self, frame_count):
        return self.get_screen(frame_count=frame_count), self.get_keys()

    def get_keys(self):
        keys_down = []
        keys_to_get = ['w', 'k', 'l', 'space']
        for key in keys_to_get:
            keys_down.append({key: keyboard.is_pressed(key)})

        return keys_down
