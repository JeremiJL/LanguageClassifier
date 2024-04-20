from network import Network

# Basic interface
print("Welcome to Language Classifier!")
# Learning rate request
learning_rate = float(input("Provide learning rate: "))
# Data request
data_directory = input("Provide data directory path: ")

# Create network
network = Network(data_directory, learning_rate)


# Loop
running = True
while running:
    option = input("\na) text classification\nb) recalculate\nc) exit\nOption : ")
    match option:
        case "a":
            text = input("Enter your text: ")
            print("Result of classification :", network.classify(text))
        case "b":
            network = Network(data_directory, learning_rate)
            # Print accuracies
            print("Accuracy of network: ", network.accuracy())
        case "c":
            running = False

