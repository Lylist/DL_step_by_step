#!/usr/bin/python
# coding=utf-8
from layer.layer_base import LayerBase
from layer.layer_sigmoid import SigmoidLayer
from layer.layer_ReLU import ReLULayer
from layer.layer_output import OutpurLayer


def cook_factory(size=0, name="", layer_type="base"):
    if layer_type is "base":
        food = LayerBase(size, 1, name)
    elif layer_type is "sigmoid":
        food = SigmoidLayer(size, 1, name)
    elif layer_type is "relu":
        food = ReLULayer(size, 1, name)
    elif layer_type is "output":
        food = OutpurLayer(size, 1, name)
    else:
        raise Exception("This network don't have {} layer model".format(layer_type))
    return food
