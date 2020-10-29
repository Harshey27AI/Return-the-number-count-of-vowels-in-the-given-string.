# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:55:20 2020

@author: harsh
"""


def get_count(input_str):
   
    return (sum(input_str.count(items) for items in ("a","e","i","o","u")))