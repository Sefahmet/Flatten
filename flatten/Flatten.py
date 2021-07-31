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

def inverse(list_1):
    new_list = list_1[::-1]
    for index, item in enumerate(new_list):
        if type(item)==list:
            new_list[index] = item[::-1]
        else:
            pass
    return new_list