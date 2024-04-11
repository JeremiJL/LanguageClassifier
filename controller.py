from converter import Converter
from perceptron import Perceptron


class Controller:

    def __init__(self, data_dir):
        # Converter responsible for converting ASCII text into vectors
        self.converter = Converter(data_dir)
        # Stores number of classes - number of perceptron the layer consist of
        self.num_of_classes = self.converter.get_num_of_classes()
        # Store train set
        self.train_test = self.converter.get_train_set()
        # Store test set
        self.test_set = self.converter.get_test_set()
        # Store perceptron in map : class -> perceptron
        self.perceptron_map = self.create_perceptrons

    def create_perceptrons(self):
        pass