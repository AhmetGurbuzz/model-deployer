from typing import List


class ModelDeployer:
    def __init__(self, features: List[str], predict, calibrate):
        self.features = features
        self.predict = predict
        self.calibrate = calibrate
