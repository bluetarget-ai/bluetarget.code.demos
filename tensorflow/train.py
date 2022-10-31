import tensorflow as tf

# Creates tensorflow model
model = tf.keras.applications.ResNet50V2(
    include_top=True,
    weights="imagenet",
    classifier_activation="softmax",
)

model.save('my_model')
