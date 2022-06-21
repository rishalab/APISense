from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib
import tensorflow as tf
from six.moves import xrange  # pylint: disable=redefined-builtin

assert tf.__version__ == "1.8.0"
tf.set_random_seed(20180130)

# Global constants describing the CIFAR-10 data set.
NUM_CLASSES = 10
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = 5000
NUM_EXAMPLES_PER_EPOCH_FOR_EVAL = 1000
IMAGE_SIZE = 32


sess = tf.InteractiveSession()
train_data, train_labels = inputs(False, "data", 6000)
print(train_data, train_labels)
train_data = train_data.eval()
train_labels = train_labels.eval()
print(train_data)
print(train_labels)
sess.close()
