#!/usr/bin/python
# coding=utf-8
import numpy as np


class LayerBase:

    def __init__(self, shape=(1, 1), b=0):
        self.shape = shape
        self.b = b
        self.W = np.zeros(shape)
        self.X = np.zeros(shape[0])
        self.Y = np.zeros()

    def activation_function(self, x):
        """
        用于神经元激活
        :param x: 输入
        :return: 输出
        """
        pass

    def cal(self, pre):
        """
        计算当前层神经元
        :param pre: 上层网络
        :return: void
        """
