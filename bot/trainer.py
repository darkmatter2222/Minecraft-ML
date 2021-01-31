import os
import zipfile
from tensorflow.keras import layers
from tensorflow.keras import Model
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

save_root = 'n:\\minecraft-ml\\training'
model_root = 'n:\\minecraft-ml\\models'
space_root = f'{save_root}\\space'
left_root = f'{save_root}\\left'
right_root = f'{save_root}\\right'

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

make_dir(model_root)

image_generator = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = image_generator.flow_from_directory(
        save_root,
        target_size=(640, 480),
        batch_size=10,
        shuffle=True,
        subset="training",
        class_mode='categorical')

validation_generator = image_generator.flow_from_directory(
        save_root,
        target_size=(640, 480),
        batch_size=10,
        shuffle=True,
        subset="training",
        class_mode='categorical')

#test1, test2 = train_generator.next()

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(640, 480, 3)),
    tf.keras.layers.Conv2D(16, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(64, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(4, activation=tf.nn.sigmoid)
])

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['accuracy'])

history = model.fit(
      train_generator,
      steps_per_epoch=train_generator.samples/train_generator.batch_size,
      epochs=2,
      validation_data=validation_generator,
      validation_steps=validation_generator.samples/validation_generator.batch_size,
      verbose=1)

model.save(f'{model_root}\\MCModel1.h5')
