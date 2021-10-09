from .model_deployer import ModelDeployer
from .util import load_model, save_model
from .exceptions import IsNotList, IsNotFunction

import pickle
import cloudpickle


PICKLE = 'pickle'
CLOUDPICKLE = 'cloudpickle'
pickling = {
    PICKLE: pickle,
    CLOUDPICKLE: cloudpickle
}