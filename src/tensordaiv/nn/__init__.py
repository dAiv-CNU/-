from keras import *


class Model:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__init__(*args, **kwargs)
        input_example = Input(shape=self.input_size)
        return models.Model(inputs=input_example, outputs=self.call(input_example))

    def __init__(self, input_size, *args, **kwargs):
        self.input_size = input_size

    def call(self, *args, **kwargs):
        pass
