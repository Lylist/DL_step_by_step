#!/usr/bin/python
# coding=utf-8
import numpy as np


class LayerBase:

    def __init__(self, size=0, b=0, name="", layer_type="base"):
        self.size = size
        self.b = b
        self.W = None
        self.Y = np.zeros(size)
        self.pre = None
        self.Name = name
        self.type = layer_type

    def activation_function(self, x):
        """
        用于神经元激活
        :param x: 输入
        :return: 输出
        """
        pass

    def cal(self):
        """
        计算当前层神经元
        :return: void
        """
        if self.pre is None:
            raise Exception("{} layer's pre-layer have error".format(self.Name))

        try:
            self.Y = np.dot(self.pre.Y, self.W) + self.b
            self.Y = self.activation_function(self.Y)
        except Exception as e:
            print(e)
            raise Exception("{} layer update value has error".format(self.Name))


