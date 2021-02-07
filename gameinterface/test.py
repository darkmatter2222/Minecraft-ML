from gameinterface import minecraftinterface
import cv2
from PIL import Image


def render_image(image):
    image, gif_image = concat_images(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = scale_down_image(image)
    cv2.imshow('Python Screen Grab', image)
    cv2.waitKey(1)


def scale_down_image(image):
    scale_percent = 25
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    return cv2.resize(image, (width, height))


def concat_images(image):
    images = []
    pil_images = []
    if image.shape[3] is not None and image.shape[3] > 1:
        for image_index in range(image.shape[3]):
            images.append(image[:, :, :, image_index])
            pil_images.append(Image.fromarray(image[:, :, :, image_index]))
    vert_image = cv2.vconcat(images)
    #pil_images[0].save('out.gif', save_all=True, append_images=pil_images)
    return vert_image


mci = minecraftinterface.Win10MinecraftApp()



while True:
    sc = mci.get_screen(5)
    if sc is not None:
        render_image(sc)
        image = Image.fromarray(sc)
