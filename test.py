from gameinterface import minecraftinterface
import cv2

def render_image(image):
    new_image = [image.shape[0] * image.shape[3], image.shape[1], image.shape[2]]

    for x in range(1, image.shape[3] + 1):
        this_image = image[:, :, :, x-1]
        int_test = image.shape[0]
        new_image[0, :, :] = this_image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow('Python Screen Grab', image)
    cv2.waitKey(1)



mci = minecraftinterface.Win10MinecraftApp()
for x in range(0, 100000000):
    sc = mci.get_screen(5)
    if not sc is None:
        render_image(sc)

