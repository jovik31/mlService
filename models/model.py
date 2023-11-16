
class Model:

    def __init__(self, name, hyperparameters, model):
        self.name = name
        self.hyperparameters = hyperparameters
        self.model = model

    def __call__(self):
        return self.model
