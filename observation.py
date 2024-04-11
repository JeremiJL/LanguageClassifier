class Observation:

    def __init__(self, label, attributes_values, ):
        # Name of the class
        self.label = label
        # Vector storing attribute values
        self.values = attributes_values

    def get_dimensions(self):
        # Number of attributes - number of dimension
        return len(self.values)

    def __str__(self):
        return "Observation :\tLabel : " + self.label + ". Attributes-Vector : " + str(self.values)
