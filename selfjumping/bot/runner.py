from selfwalking.gameinterface import minecraftinterface
import tensorflow as tf
import keyboard
import numpy as np

mci = minecraftinterface.Win10MinecraftApp()

model_root = 'n:\\minecraft-ml\\models'

model = tf.keras.models.load_model(f'{model_root}\\MCModel1.h5')

while True:
    screen = mci.get_screen()

    screen = screen.resize((320, 240))

    screen = np.array(screen) / 225

    result = model.predict(np.array([screen]))

    actions = ['left', 'none', 'right', 'space']

    directives = {'left': 'k', 'right': 'l', 'space': 'space', 'none': 'DONOTHING'}

    action = actions[np.argmax(result)]

    key = directives[action]
    if keyboard.is_pressed('ctrl'):
        if not key == 'DONOTHING':
            mci.send_keystroke([{'action': 'press_and_release', 'key': key}])

    print(np.argmax(result))
