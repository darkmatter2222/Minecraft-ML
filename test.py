from gameinterface import minecraftinterface
import cv2

def render_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow('Real Time Play', image)
    cv2.waitKey(1)



mci = minecraftinterface.Win10MinecraftApp()
for x in range(0, 100000000):
    sc = mci.get_screen()
    if not sc is None:
        render_image(sc)

