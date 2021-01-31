import win32gui


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
        self.top_windows = []
        self.minecraft = []
        win32gui.EnumWindows(window_enumeration_handler, self.top_windows)
        for i in self.top_windows:
            if "minecraft" == i['app'][1].lower():
                self.minecraft = i
                break

        if not self.minecraft:
            raise Exception("Windows 10 Minecraft found to not be running,"
                            "Make sure Windows 10 Minecraft is running and "
                            "your world is loaded")





