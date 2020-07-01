#!/usr/bin/python
# coding=utf-8
import numpy as np
from layer.layer_base import LayerBase


class SigmoidLayer(LayerBase):

    def __init__(self, size=0, b=0, name=""):

        LayerBase.__init__(self, size, b, name, layer_type="sigmoid")

    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def activation_function(self, x):
        """
        simoid函数判断
        :param x:
        :return:
        """
        return self.__sigmoid(x)
