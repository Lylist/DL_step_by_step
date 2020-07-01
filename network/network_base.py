#!/usr/bin/python
# coding=utf-8
import numpy as np
from layer.layer_base import LayerBase


class NetworkBase:

    def __init__(self, name="myDNN"):
        self.Name = name
        self.layers = []
        self.layer_type_dict = {}

    @staticmethod
    def __link_layer(pre, post):
        """
        连接相邻两层
        :param pre:前
        :param post: 后
        :return: bool
        """
        post.pre = pre
        post.W = np.ones(pre.size, post.size)

    def add(self, layer_type, size, name=""):
        """
        网络添加新的层
        :param layer_type:层的类型，enum
        :param size:层大小，int
        :param name:名字，string，default：type_{id}
        :return:
        """
        if self.layer_type_dict.get(layer_type):
            self.layer_type_dict[layer_type] += 1
        else:
            self.layer_type_dict[layer_type] = 0
        if name is "":
            name = layer_type + str(self.layer_type_dict[layer_type])

        if layer_type == 'base':
            new_layer = LayerBase(size, 0, name)
        else:


        if len(self.layers) > 0:
            self.__link_layer(self.layers[-1], new_layer)
        self.layers.append(new_layer)


