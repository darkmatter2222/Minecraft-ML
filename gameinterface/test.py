from gameinterface import minecraftinterface
import cv2


def render_image(image):
    image = concat_images(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = scale_down_image(image)
    cv2.imshow('Python Screen Grab', image)
    cv2.waitKey(1)

def scale_down_image(image):
    scale_percent = 50
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    return cv2.resize(image, (width, height))

def concat_images(image):
    images = []
    if image.shape[3] is not None and image.shape[3] > 1:
        for image_index in range(image.shape[3]):
            images.append(image[:, :, :, image_index])
    return cv2.vconcat(images)

mci = minecraftinterface.Win10MinecraftApp()
while True:
    sc = mci.get_screen(5)
    if sc is not None:
        render_image(sc)
