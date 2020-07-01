#!/usr/bin/python
# coding=utf-8
import numpy as np
from layer.layer_base import LayerBase


class OutpurLayer(LayerBase):

    def __init__(self, size=0, b=0, name=""):
        LayerBase.__init__(self, size, b, name, layer_type="output")

    def activation_function(self, x):
        """
        恒等输出
        :param x:
        :return:
        """
        return x
