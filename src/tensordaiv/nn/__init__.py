from keras import *
from keras.src.utils.naming import auto_name


class Model:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__init__(*args, **kwargs)

        input_example = Input(shape=self.input_size)
        model = models.Model(inputs=input_example, outputs=self.call(input_example), name=auto_name(cls.__name__))

        model.__dict__['__name__'] = cls.__name__
        model.__dict__['__module__'] = cls.__module__
        model.__dict__['__qualname__'] = cls.__qualname__
        model.__dict__['__doc__'] = cls.__doc__

        return model

    def __init__(self, input_size, *args, **kwargs):
        self.input_size = input_size

    def call(self, *args, **kwargs):
        pass
