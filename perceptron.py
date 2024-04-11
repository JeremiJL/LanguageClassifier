from observation import Observation
from random import shuffle, random


def return_key_by_value(dictionary, searched_value):
    for key, value in dictionary.items():
        if value == searched_value:
            return key


def dot_product(vector, weights):
    result = 0
    for x, y in zip(vector, weights):
        result += x * y
    return result


def heavy_side(y):
    if y > 0:
        return 1
    else:
        return 0


def delta_update_weights(direction, learning_rate, vector, weights):
    for v, i in zip(vector, range(len(vector))):
        weights[i] += direction * learning_rate * v


class Perceptron:
    def __init__(self, train_set, test_set, learning_rate, epochs):
        # Assign
        self.train_set = train_set
        self.test_set = test_set
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.accuracy_list = []
        self.weights = None
        self.finished = False
        # Start time-consuming tasks
        self.begin()

    def begin(self):
        # Initialize starter weights
        self.weights = self.initialize_starter_weights()
        self.num_of_dimensions = self.train_set[0].num_of_attributes
        # Train
        self.train()
        # Test
        self.test()
        #  After whole training process is completed raise flag
        self.finished = True

    def train(self):
        # Iterate 'epoch' number of times
        for epoch in range(0, self.epochs):

            for observation in self.observations:
                vector = observation.values
                y = self.classify(vector)
                # y - computed result of classification, d - desired result of classification
                d = self.classes_map[observation.label]
                # Check if the result corresponds with the observation class
                # If it doest match apply delta rule
                if y != d:
                    direction = d - y
                    delta_update_weights(direction, self.learning_rate, vector, self.weights)

            # After each iteration shuffle the order of observations
            shuffle(self.observations)
            # After each epoch calculate the accuracy
            self.accuracy_list.append(self.evaluate_accuracy())


    def classify(self, vector):
        # add constant value at index 0 if needed
        if len(vector) != self.num_of_dimensions + 1:
            vector.insert(0,1)
        # Calculate the dot product between vector and weights
        # (treshold included in formula as a constant element of vector and weights)
        y = dot_product(tuple(vector), tuple(self.weights))
        # Perform the heavy side function
        return heavy_side(y)

    def evaluate_accuracy(self):
        # Store number of successful tests
        successes = 0
        total = len(self.test_observations)
        # Classify each observation from test observations list
        # It the outcome of classification will be just as desired increment successes counter
        for observation in self.test_observations:
            vector = observation.values
            y = self.classify(vector)
            # y - computed result of classification, d - desired result of classification
            d = self.classes_map[observation.label]
            # If computed class equals the true one (desired) then it is a success
            if y == d:
                successes += 1

        # Return the classification accuracy
        return successes/total

    def initialize_starter_weights(self):
        # threshold - also known as bias
        bias = 1.5
        weights = [(random() + 1) / 10 for _ in range(self.num_of_dimensions)]
        weights.insert(0, bias)
        return weights


    def test(self):
        pass
