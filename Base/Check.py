__author__ = 'Administrator'
import os, sys
class base_check:
    def __init__(self, param=None, index=None):
        self.param = param
        self.index = index

    def check_index(self):
        if type(self.param) == dict:
            if self.param.get(self.index, "default") == "default":
                return False
            return True
        if type(self.param) == list:
            if self.index in self.param:
                return True
            return False

