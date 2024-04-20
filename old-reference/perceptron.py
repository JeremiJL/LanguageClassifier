# from observation import Observation
# from random import shuffle, random
#
#
# def dot_product(vector, weights):
#     result = 0
#     for x, y in zip(vector, weights):
#         result += x * y
#     return result
#
#
# def heavy_side(y):x
#     if y > 0:
#         return 1
#     else:
#         return 0
#
#
# def delta_update_weights(direction, learning_rate, vector, weights):
#     for v, i in zip(vector, range(len(vector))):
#         weights[i] += direction * learning_rate * v
#
#
# class Perceptron:
#
#     def __init__(self, train_set, test_set, perceptron_class, learning_rate=0.1, epochs=20):
#         # Assign
#         self.perceptron_class = perceptron_class
#         self.train_set = train_set
#         self.test_set = test_set
#         self.learning_rate = learning_rate
#         self.epochs = epochs
#         self.accuracy_list = []
#         self.weights = None
#         self.finished = False
#         self.dimensions = None
#         # Start time-consuming tasks
#         self.begin()
#
#     def begin(self):
#
#         # Order of execution is important
#         # Extract number of dimensions from first observations in list
#         self.dimensions = self.train_set[0].get_dimensions()
#         # Initialize starter weights
#         self.weights = self.initialize_starter_weights()
#         # Adjust observations - prepare them to work with perceptron
#         # It modifies their number of dimensions by 1
#         self.adjust_observations()
#
#         # Train
#         self.train()
#         # Test TMP
#         self.test()
#         # After whole training process is completed raise flag
#         self.finished = True
#
#     def train(self):
#         # Iterate 'epoch' number of times
#         for epoch in range(0, self.epochs):
#
#             for observation in self.train_set:
#                 # we work on vector - values of attributes
#                 vector = observation.values
#                 # y - computed result of classification
#                 # 1 or 0 depending on dot product result
#                 y = heavy_side(self.classify(vector))
#                 # d - desired result of classification
#                 # 0 if the label is the one for which this perceptron should be activated
#                 # 1 if it's some other label
#                 d = self.label_comparison_numerical(observation.label)
#                 # Check if the result corresponds with the observation class
#                 # If it doest match apply delta rule
#                 if y != d:
#                     direction = d - y
#                     delta_update_weights(direction, self.learning_rate, vector, self.weights)
#
#             # After each iteration shuffle the order of observations
#             shuffle(self.train_set)
#             # After each epoch calculate the accuracy
#             self.accuracy_list.append(self.evaluate_accuracy())
#
#     def classify(self, vector):
#         # add constant value at index 0 if needed
#         if len(vector) != self.dimensions + 1:
#             vector.insert(0, 1)
#
#         # Calculate the dot product between vector and weights
#         # (threshold included in formula as a constant element of vector and weights)
#         return dot_product(tuple(vector), tuple(self.weights))
#
#     def evaluate_accuracy(self):
#         # Store number of successful tests
#         successes = 0
#         total = len(self.test_set)
#         # Classify each observation from test observations list
#         # It the outcome of classification will be just as desired increment successes counter
#         for observation in self.test_set:
#             vector = observation.values
#             # y - computed result of classification
#             y = heavy_side(self.classify(vector))
#             # d - desired result of classification
#             d = self.label_comparison_numerical(observation.label)
#             # If computed class equals the true one (desired) then it is a success
#             if y == d:
#                 successes += 1
#
#         # Return the classification accuracy
#         return successes / total
#
#     def initialize_starter_weights(self):
#         # threshold - also known as bias
#         bias = 1.5
#         # weights = [(random() + 1) / 10 for _ in range(self.dimensions)]
#         # weights = [float((random() + 1) / 10.) for _ in range(self.dimensions)]
#         weights = [0.1 for _ in range(self.dimensions)]
#         weights.insert(0, bias)
#         return weights
#
#     def adjust_observations(self):
#         # Add constant 1 on first index of each observation
#         # For observations in train set
#         for observation in self.train_set:
#             observation.values.insert(0, 1)
#         # For observations in test set
#         for observation in self.test_set:
#             observation.values.insert(0, 1)
#
#     def label_comparison_numerical(self,label):
#         if label == self.perceptron_class:
#             d = 0
#         else:
#             d = 1
#
#         return d
#
#     def test(self):
#         pass
