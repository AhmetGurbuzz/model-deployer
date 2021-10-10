from modeldeployer.model_deployer import ModelDeployer
from modeldeployer.util import load_model, save_model
from modeldeployer.exception import IsNotList, IsNotFunction

import pickle
import cloudpickle


PICKLE = 'pickle'
CLOUDPICKLE = 'cloudpickle'
pickling = {
    PICKLE: pickle,
    CLOUDPICKLE: cloudpickle
}