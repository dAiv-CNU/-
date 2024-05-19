from keras import *


class Model:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__init__(*args, **kwargs)
        input_example = Input(shape=self.input_size)
        return Model(inputs=input_example, outputs=self.call(input_example))

    def __init__(self, input_size):
        self.input_size = input_size

    def call(self, inputs, silent=False):
        pass
