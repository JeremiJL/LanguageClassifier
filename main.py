from converter import Converter
from controller import Controller
import matplotlib

controller = Controller("observations_data", epochs=30)

text = input("enter text : \n")

observation = controller.get_converter().convert_text(text)
print("classification of your text", controller.classify(observation) )