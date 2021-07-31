# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:22:10 2021

@author: Sefa
"""

lst = []
def flatten(list_):
    for item in list_:
        if type(item) != list:
            lst.append(item)
        else:
            flatten(item)
    return lst