import os
from typing import Dict, List
from scipy.special import softmax
import requests
import tempfile
import numpy as np
import tensorflow as tf

from tensorflow import keras


class Model:

    labels: None

    def __init__(self) -> None:
        self._model = None
        self.labels = requests.get(
            'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
        ).text.split('\n')

    def load(self):
        self._model = keras.models.load_model(
            f"{os.path.dirname(__file__)}/my_model")

    def preprocess(self, image_url: str):
        request = requests.get(image_url)
        with tempfile.NamedTemporaryFile() as f:
            f.write(request.content)
            f.seek(0)
            input_image = tf.image.decode_png(tf.io.read_file(f.name))
        preprocessed_image = tf.keras.applications.resnet_v2.preprocess_input(
            tf.image.resize([input_image], (224, 224))
        )
        return np.array(preprocessed_image)

    def postprocess(self, predictions, k=5):
        class_predictions = predictions[0]
        class_probabilities = softmax(class_predictions)
        top_probability_indices = class_probabilities.argsort()[
            ::-1][:k].tolist()
        return {self.labels[index]: 100 * class_probabilities[index].round(3) for index in top_probability_indices}

    def predict(self, request: Dict) -> Dict[str, List]:

        inputs = request["inputs"]
        predictions = []

        for input in inputs:

            input = self.preprocess(input)
            prediction = self._model.predict(input).tolist()
            prediction = self.postprocess(prediction)
            predictions.append(prediction)

        return {
            "predictions": predictions
        }
