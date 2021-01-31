from gameinterface import minecraftinterface
import os
import random
import uuid

mci = minecraftinterface.Win10MinecraftApp()

save_root = 'n:\\minecraft-ml\\training'
space_root = f'{save_root}\\space'
left_root = f'{save_root}\\left'
right_root = f'{save_root}\\right'
none_root = f'{save_root}\\none'


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

make_dir(save_root)
make_dir(space_root)
make_dir(left_root)
make_dir(right_root)
make_dir(none_root)

while True:
    screen, keys = mci.get_screen_and_keys()

    if not {'w': True} in keys:
        continue

    if {'space': True} in keys:
        screen.save(f'{space_root}\\{uuid.uuid1()}.png')
    elif {'left': True} in keys:
        screen.save(f'{left_root}\\{uuid.uuid1()}.png')
    elif {'right': True} in keys:
        screen.save(f'{right_root}\\{uuid.uuid1()}.png')
    else:
        if random.random() > 0.5:
            screen.save(f'{none_root}\\{uuid.uuid1()}.png')



    print(keys)