import os
from typing import Dict, List

DEBUG = bool(os.environ.get("debug", False))


class Model:
    def __init__(self) -> None:
        self._model = None

    def load(self):
        import pickle

        with open(f"{os.path.dirname(__file__)}/model.pkl", 'rb') as pickle_file:
            self._model = pickle.load(pickle_file)

    def predict(self, request: Dict) -> Dict[str, List]:

        if DEBUG == True:
            print("Debug enabled")

        response = {}
        inputs = request["inputs"]
        result = self._model.predict(inputs).tolist()
        response["predictions"] = result

        return response
