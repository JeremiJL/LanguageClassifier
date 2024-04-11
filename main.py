from converter import Converter
import matplotlib
converter = Converter("observations_data")


print("---TRAIN SET")
for o in converter.get_train_set():
    print("label:", o.label, "dimensions:", len(o.values), "values:", o.values, end="\n")



print("---TEST SET")
for o in converter.get_test_set():
    print("label:", o.label, "dimensions:", len(o.values), "values:", o.values, end="\n")

