#!/usr/bin/python
# coding=utf-8
import numpy as np
from layer.layer_base import LayerBase


class ReLULayer(LayerBase):

    def __init__(self, size=0, b=0, name=""):
        LayerBase.__init__(self, size, b, name, layer_type="relu")

    def __relu(self, x):
        return np.maximum(0, x)

    def activation_function(self, x):
        """
        ReLU函数判断
        :param x:
        :return:
        """
        return self.__relu(x)