from converter import Converter
from controller import Controller
import matplotlib

controller = Controller("observations_data", epochs=30)
# observation = controller.test_set[0]
# print("true result:", observation.label)
# print("result of classification:", controller.classify(observation.values))
# print(controller.accuracy())

# print("---TRAIN SET")
# for o in converter.get_train_set():
#     print("label:", o.label, "dimensions:", len(o.values), "values:", o.values, end="\n")
# print("---TEST SET")
# for o in converter.get_test_set():
#     print("label:", o.label, "dimensions:", len(o.values), "values:", o.values, end="\n")

text = input("enter text")

observation = controller.get_converter().convert_text(text)
print("classification of your text", controller.classify(observation) )