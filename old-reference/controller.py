from converter import Converter
from perceptron import Perceptron


class Controller:

    def __init__(self, data_dir, learning_rate=0.1, epochs=20):
        # Learning rate of perceptrons
        self.learning_rate = learning_rate
        # Number of epochs for each perceptron
        self.epochs = epochs
        # Converter responsible for converting ASCII text into vectors
        self.converter = Converter(data_dir)
        # Stores number of classes - number of perceptron the layer consist of
        self.num_of_classes = self.converter.get_num_of_classes()
        # Store classes names - labels
        self.labels = self.converter.get_labels()
        # Store train set
        self.train_test = self.converter.get_train_set()
        # Store test set
        self.test_set = self.converter.get_test_set()
        # Store perceptron in map : class -> perceptron
        self.perceptron_map = dict()

        # Initialize models
        self.create_perceptrons()
        # self.train_perceptrons()

    def create_perceptrons(self):
        # Create and train perceptrons for each class, responsible for this one class
        for label in self.labels:
            perceptron = Perceptron(label, list.copy(self.train_test), list.copy(self.test_set), self.learning_rate,
                                    self.epochs)
            self.perceptron_map[label] = perceptron

    def classify(self, observation):
        # Result-Label dictionary maps results of classification of each perceptron and their labels
        # value -> label
        result_label_map = dict()
        for label in self.labels:
            value = self.perceptron_map.get(label).classify(observation)
            result_label_map[value] = label

        # The greatest value in dictionary corresponds with result of classification
        # Find the greatest value
        max_val = max(result_label_map.keys())
        # Return corresponding label with this value
        # print(result_label_map)
        return result_label_map.get(max_val)

    def accuracy(self):
        # Store accuracies of perceptrons in perceptron -> accuracy map
        accuracies = dict()
        # For each perceptron compute accuracy
        for label in self.labels:
            accuracies[label] = self.perceptron_map.get(label).evaluate_accuracy()

        # Return accuracies of each perceptron
        return accuracies

    def get_converter(self):
        return self.converter
