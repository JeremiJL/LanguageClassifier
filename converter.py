import os

import random

from observation import Observation


def create_proportion_map():
    proportion_map = dict()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        proportion_map[letter] = 0

    return proportion_map


def sum_of_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    return total_sum


class Converter:

    def __init__(self, directory):
        # Percentage of how many observations train set consist of from all observations
        # The rest of observations builds the test set
        self.proportion_of_train_set = 0.90
        # Ascii : proportion map
        self.empty_proportion_map = create_proportion_map()
        # Observations_data directory
        self.directory_path = directory
        # Store classes names
        self.labels = list()
        # Number of classes
        self.num_of_classes = 0
        # Store part of all observations as train set
        self.train_set = list()
        # Store complement of observations as test set
        self.test_set = list()
        # Store all converted observations
        self.observations = list()
        # Compute - Convert
        self.compute()

    def compute(self):
        # Computational part in correct order
        self.labels = self.determine_labels()
        self.observations = self.convert_observations()
        self.num_of_classes = len(self.labels)

    def determine_labels(self):
        return [str(dir) for dir in os.listdir(self.directory_path)]

    def get_labels(self):
        return self.labels

    def get_num_of_classes(self):
        return self.num_of_classes

    def get_train_set(self):
        # Train set consists of x% of all observations
        return self.train_set

    def get_test_set(self):
        # Test set consists of (100-x)% of all observations
        return self.test_set

    def convert_text(self, text):
        # Proportion map
        proportions = self.empty_proportion_map.copy()

        # Iterate over each letter of text
        for letter in text:
            # Values set of proportions map will correspond to attribute values of observation
            # Divide numbers of occurrences by number of all letters
            if letter in proportions.keys():
                proportions[letter] += 1

        num = sum_of_values(proportions)
        values = [v / num for v in proportions.values()]

        # return vector of values
        return values

    def convert_observations(self):

        # Observations list
        observations = list()

        # Proportion map
        proportions = self.empty_proportion_map.copy()

        # Each directory consist of multiple files in certain language
        directories = [self.directory_path + "\\" + d for d in os.listdir(self.directory_path)]
        directories_labels_map = dict()
        for directory, label in zip(directories, self.labels):
            directories_labels_map[directory] = label

        # Iterate over each file of each directory
        for directory in directories:
            files = [f for f in os.listdir(directory)]
            for file in files:
                file_path = os.path.join(directory, file)
                with open(file_path, "r", encoding='utf-8') as text:
                    for line in text:
                        # Make all characters in lowercase
                        line = line.lower()
                        for letter in line:
                            if letter in proportions.keys():
                                proportions[letter] += 1
                    # Values set of proportions map will correspond to attribute values of observation
                    # Divide numbers of occurrences by number of all letters
                    num = sum_of_values(proportions)
                    values = [v / num for v in proportions.values()]
                    # Extract label name from file path
                    label = directories_labels_map[directory]
                    # Create observation
                    observations.append(Observation(label, values))

        # Shuffle the observations inside the list
        # Obligatory step before dividing between train and test set
        random.shuffle(observations)
        # Divide observation list for train set and test set
        num_of_observations = len(observations)
        volume_of_train_set = int(self.proportion_of_train_set * num_of_observations)

        self.train_set = observations[0:volume_of_train_set]
        self.test_set = observations[volume_of_train_set:]

        # Return completed list of converted observations
        return observations
