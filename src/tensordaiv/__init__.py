from tensorflow import *
try:
    tf_nn = nn
    del nn
finally:
    from . import nn
