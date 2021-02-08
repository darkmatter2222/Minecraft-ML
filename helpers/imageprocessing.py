import cv2
from PIL import Image


def concat_images(np_images):
    images = []
    if np_images.shape[3] is not None and np_images.shape[3] > 1:
        for image_index in range(np_images.shape[3]):
            images.append(np_images[:, :, :, image_index])
    else:
        raise Exception('Muli Image Required')

    return cv2.vconcat(images)


def scale_down_image(np_image):
    scale_percent = 25
    width = int(np_image.shape[1] * scale_percent / 100)
    height = int(np_image.shape[0] * scale_percent / 100)
    return cv2.resize(np_image, (width, height))


def array_to_image(np_image):
    return Image.fromarray(np_image)