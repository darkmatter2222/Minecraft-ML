from gameinterface import minecraftinterface
import tensorflow as tf
from PIL import Image
import numpy as np

mci = minecraftinterface.Win10MinecraftApp()

model_root = 'n:\\minecraft-ml\\models'

model = tf.keras.models.load_model(f'{model_root}\\MCModel1.h5')

while True:
    screen = mci.get_screen()

    screen = screen.resize((640,480))

    screen = np.array(screen) / 225

    result = model.predict(np.array([screen]))

    print(result)
