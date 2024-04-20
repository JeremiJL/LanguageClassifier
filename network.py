import math
from random import random, shuffle

from converter import Converter


class Network:

    def __init__(self, data_dir, learning_rate=0.01):
        # Learning rate of perceptrons
        self.learning_rate = learning_rate
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
        # Extract number of dimensions from first observations in list
        self.dimensions = self.train_test[0].get_dimensions()
        # Accuracy
        self.accuracy = 0

        # Initialize models
        self.create_perceptrons()
        # Train model
        self.train()

    def create_perceptrons(self):
        # Create and train perceptrons for each class, responsible for this one class
        for label in self.labels:
            perceptron = Perceptron(label, self.dimensions)
            self.perceptron_map[label] = perceptron

    def classify(self, text_input):

        # Classify input text from user
        vector = self.converter.convert_text(text_input)

        # Dictionary maps result of dot product with class labels
        outcome_label_map = dict()

        # Calculate dot product for each perceptron
        for perceptron in self.perceptron_map.values():
            outcome = perceptron.dot_product(vector)
            outcome_label_map[outcome] = perceptron.label

        # Find the greatest value of outcomes of dot product and map it corresponding label
        greatest = max(outcome_label_map.keys())
        result_of_classification = outcome_label_map.get(greatest)

        return result_of_classification

    def train(self):

        # Keep record of epochs
        epoch = 0

        # Train the neural network until accuracy reaches 100%
        while self.accuracy != 1:

            accuracy_of_iteration = 0

            # shuffle the data in train set
            shuffle(self.train_test)

            # Iterate over every observation from train set
            for observation in self.train_test:

                # The label we are considering in this iteration
                target = observation.label

                # Dictionary maps labels of classes and dot product of assigned perceptrons
                label_outcome_map = dict()

                # Fill dictionary with values
                for key, value in zip(self.perceptron_map.keys(), self.perceptron_map.values()):
                    label_outcome_map[key] = self.perceptron_map[key].dot_product(observation.values)

                # Determine which perceptron produced the dot product with the highest value
                greatest_perceptron_label = target
                greatest_dot_product = label_outcome_map[target]

                for label, product in zip(label_outcome_map.keys(), label_outcome_map.values()):
                    if product > greatest_dot_product:
                        greatest_dot_product = product
                        greatest_perceptron_label = label

                # If the target label and the label of perceptron which produced the highest dot product
                # is the same, then it is a successful iteration, increment accuracy

                # If the target label doesn't match the label of the perceptron that produced the highest
                # dot product, then we should apply delta rule on each perceptron.
                # For the perceptron that should have fired, but didn't, we apply delta rule with positive sign
                # For the perceptron that fired we apply delta rule with negative sign

                if greatest_perceptron_label == target:
                    accuracy_of_iteration += 1
                else:
                    # negative delta rule
                    self.perceptron_map[greatest_perceptron_label].delta_update_weights(-1, self.learning_rate,
                                                                                        observation.values)
                    # positive delta rule
                    self.perceptron_map[target].delta_update_weights(1, self.learning_rate, observation.values)

            # Normalize all weights vectors after each epoch
            for perceptron in self.perceptron_map.values():
                perceptron.normalize_weights()

            # divide the accuracy over number of train set
            self.accuracy = float(accuracy_of_iteration / len(self.train_test))
            # Inform about epoch number and accuracy
            epoch += 1
            print("Epoch :", str(epoch), " - Accuracy :", str(self.accuracy * 100) + "%")

            self.test_print()

    def test_print(self):
        print("Weights changes :")
        for perceptron in self.perceptron_map.values():
            print(perceptron.label, " - weights :", perceptron.weights)


class Perceptron:
    # local architecture
    def __init__(self, label, dimensions):
        # class of this perceptron
        self.label = label
        # number of dimensions of observation data
        self.dimensions = dimensions
        # weights
        self.weights = self.initialize_weights()

    def initialize_weights(self):
        # threshold - also known as bias
        bias = 1
        weights = [(random() + 1) / 10 for _ in range(self.dimensions)]
        weights.insert(0, bias)
        return weights

    def dot_product(self, vector):
        result = 0
        for x, y in zip(vector, self.weights):
            result += x * y
        return result

    def delta_update_weights(self, direction, learning_rate, vector):
        for v, i in zip(vector, range(len(vector))):
            self.weights[i] += direction * learning_rate * v

    def normalize_weights(self):
        # compute vector euclidean distance
        vector_length = 0
        for i in self.weights:
            vector_length += math.pow(i,2)

        # compute square root of length
        vector_length = math.sqrt(vector_length)
        # update vector values
        self.weights = [v/vector_length for v in self.weights]
