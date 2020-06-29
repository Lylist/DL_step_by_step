#!/usr/bin/python
# coding=utf-8
import numpy as np
from layer import *


class NetworkBase:

    def __init__(self, name="myDNN"):
        self.Name = name
        self.layers = []
        self.layer_type_dict = {}

    def add(self, layer_type, size, name=""):
        """
        网络添加新的层
        :param layer_type:层的类型，enum
        :param size:层大小，int
        :param name:名字，string，default：type_{id}
        :return:
        """