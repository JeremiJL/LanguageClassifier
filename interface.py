from converter import Converter
from controller import Controller

# Basic interface
# Learning rate request
learning_rate = float(input("Provide learning rate: "))
# Epochs request
num_epochs = int(input("Provide number of epochs: "))
# Data request
data_directory = input("Provide data directory path: ")

# Create network
controller = Controller(data_directory, learning_rate, num_epochs)

# Print accuracies
print("Accuracy of network: ", controller.accuracy())

print("\n")
# Loop
running = True
while running:
    option = input("a) text classification\nb) recalculate\ne) exit\nOption : ")
    match option:
        case "a":
            text = input("Enter your text: ")
            vector = controller.get_converter().convert_text(text)
            print("Result of classification :", controller.classify(vector))
        case "b":
            controller = Controller(data_directory, learning_rate, num_epochs)
            # Print accuracies
            print("Accuracy of network: ", controller.accuracy())
        case "c":
            running = False

