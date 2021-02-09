from gameinterface import minecraftinterface
from helpers import imageprocessing
import os
import random
import uuid

mci = minecraftinterface.Win10MinecraftApp()
mci.move_mc()
save_root = 'n:\\minecraft-ml\\selfjumping\\training'
space_root = f'{save_root}\\space'
none_root = f'{save_root}\\none'


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


make_dir(save_root)
make_dir(space_root)
make_dir(none_root)

count = 0
while True:
    np_images, keys = mci.get_screen_and_keys(frame_count=2)

    if np_images is None:
        continue

    np_image = imageprocessing.concat_images(np_images=np_images)
    np_image = imageprocessing.scale_down_image(np_image=np_image)
    imageprocessing.render_image(np_image)
    pil_image = imageprocessing.array_to_image(np_image=np_image)

    if not {'w': True} in keys:
        continue

    if {'space': True} in keys:
        pil_image.save(f'{space_root}\\{uuid.uuid1()}.png')
        print(f"Image Saved Ittr:{count}")
    else:
        if random.random() < 0.1:
            pil_image.save(f'{none_root}\\{uuid.uuid1()}.png')
            print(f"Image Saved Ittr:{count}")

    count += 1