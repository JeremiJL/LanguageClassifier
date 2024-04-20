from network import Network

# Basic interface
# Learning rate request
learning_rate = float(input("Provide learning rate: "))
# Epochs request
num_epochs = int(input("Provide number of epochs: "))
# Data request
data_directory = input("Provide data directory path: ")

# Create network
network = Network(data_directory, learning_rate)

# Print accuracies
print("Accuracy of network: ", network.accuracy())

# Loop
running = True
while running:
    option = input("a) text classification\nb) recalculate\nc) exit\nOption : ")
    match option:
        case "a":
            text = input("Enter your text: ")
            vector = network.get_converter().convert_text(text)
            print("Result of classification :", network.classify(vector))
        case "b":
            network = Network(data_directory, learning_rate, num_epochs)
            # Print accuracies
            print("Accuracy of network: ", network.accuracy())
        case "c":
            running = False

