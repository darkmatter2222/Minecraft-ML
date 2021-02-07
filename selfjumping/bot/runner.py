from gameinterface import minecraftinterface
from helpers import imageprocessing
import tensorflow as tf
import keyboard
import numpy as np
import json

if False:
    try:
        # Disable all GPUS
        tf.config.set_visible_devices([], 'GPU')
        visible_devices = tf.config.get_visible_devices()
        for device in visible_devices:
            assert device.device_type != 'GPU'
    except:
        # Invalid device or cannot modify virtual devices once initialized.
        pass

model_root = 'n:\\minecraft-ml\\selfjumping\\models'
model = tf.keras.models.load_model(f'{model_root}\\MCModel1.h5')

mci = minecraftinterface.Win10MinecraftApp()

# Classes
orig_classes = json.loads(open(f"{model_root}\\Classes.json").read())
classes = {}

for this_class in orig_classes:
    classes[orig_classes[this_class]] = this_class



while True:
    np_images = mci.get_screen(frame_count=5)

    if np_images is None:
        np_image = np.zeros([622, 2195, 3])
    else:
        np_image = imageprocessing.concat_images(np_images=np_images)

    np_image = np.array(np_image) / 225

    result = model.predict(np.array([np_image]))

    key = classes[np.argmax(result)]

    if keyboard.is_pressed('ctrl'):
        if not key == 'none':
            mci.send_keystroke([{'action': 'press_and_release', 'key': key}])

    if

    print(np.argmax(result))
