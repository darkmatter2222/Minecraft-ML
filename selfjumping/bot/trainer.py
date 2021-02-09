import os
import zipfile
from tensorflow.keras import layers
from tensorflow.keras import Model
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json
import kerastuner as kt

save_root = 'n:\\minecraft-ml\\selfjumping\\training'
model_root = 'n:\\minecraft-ml\\selfjumping\\models'


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


make_dir(model_root)

image_generator = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = image_generator.flow_from_directory(
        save_root,
        target_size=(155, 548),
        batch_size=10,
        shuffle=True,
        subset="training",
        class_mode='categorical')

validation_generator = image_generator.flow_from_directory(
        save_root,
        target_size=(155, 548),
        batch_size=10,
        shuffle=True,
        subset="training",
        class_mode='categorical')


def model_builder(hp):
    this_model = tf.keras.Sequential()
    this_model.add(tf.keras.layers.Input(shape=(155, 548, 3)))
    conv_layers = hp.Int('conv_layers', min_value=1, max_value=4, step=1)
    for index in range(conv_layers):
        this_model.add(tf.keras.layers.Conv2D(16 * (index + 1), 3, activation='relu'))
        this_model.add(tf.keras.layers.MaxPooling2D(2))

    this_model.add(tf.keras.layers.Flatten())

    dense_layer_one = hp.Int('dense_layer_one', min_value=64, max_value=512, step=2)
    this_model.add(tf.keras.layers.Dense(units=dense_layer_one, activation='relu'))

    this_model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid))

    hp_learning_rate = hp.Choice('learning_rate', values=[1e-1, 1e-2, 1e-3, 1e-4])

    this_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=hp_learning_rate),
                       loss='categorical_crossentropy',
                       metrics=['accuracy'])

    return this_model


classes = train_generator.class_indices
with open(f"{model_root}\\Classes.json", 'w') as outfile:
    json.dump(classes, outfile)
print(classes)

tuner = kt.Hyperband(model_builder,
                     objective='val_loss',
                     max_epochs=10,
                     factor=2,
                     directory='my_dir',
                     project_name='intro_to_kt9')

tuner.search(train_generator,
             epochs=50,
             validation_data=validation_generator)

best_hps = tuner.get_best_hyperparameters(num_trials=100)[0]

model = tuner.hypermodel.build(best_hps)

history = model.fit(
      train_generator,
      steps_per_epoch=train_generator.samples/train_generator.batch_size,
      epochs=10,
      validation_data=validation_generator,
      validation_steps=validation_generator.samples/validation_generator.batch_size,
      verbose=1)

model.save(f'{model_root}\\MCModel1.h5')
