# ********************************************************************************** #
#                                                                                    #
#   Project: FeatureSelect -  example on California House Prices                     #                         
#   Author: Pawel Rosikiewicz                                                        #
#   Contact: prosikiewicz(a)gmail.com                                                #
#                                                                                    #
#   License: MIT License                                                             #
#   Copyright (C) 2021.11.01 Pawel Rosikiewicz                                       #
#                                                                                    #
# Permission is hereby granted, free of charge, to any person obtaining a copy       #
# of this software and associated documentation files (the "Software"), to deal      #
# in the Software without restriction, including without limitation the rights       #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell          #
# copies of the Software, and to permit persons to whom the Software is              #
# furnished to do so, subject to the following conditions:                           #
#                                                                                    # 
# The above copyright notice and this permission notice shall be included in all     #
# copies or substantial portions of the Software.                                    #
#                                                                                    #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR         #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,           #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE        #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER             #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,      #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
# SOFTWARE.                                                                          #
#                                                                                    #
# ********************************************************************************** #


# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import random
import glob
import re
import os
import seaborn as sns

# continuous variable description, extracted from data documentation, 
CONTINUOUS_FEATURES = [
    'Lot Frontage', 'Lot Area', 'Mas Vnr Area', 'BsmtFin SF 1', 'BsmtFin SF 2',
    'Bsmt Unf SF', 'Total Bsmt SF', '1st Flr SF', '2nd Flr SF', 'Low Qual Fin SF',
    'Gr Liv Area', 'Garage Area', 'Wood Deck SF', 'Open Porch SF', 'Enclosed Porch',
    '3Ssn Porch', 'Screen Porch', 'Pool Area', 'Misc Val', "SalePrice"]


# ordinal variable description, extracted from data documentation, 
ORDINAL_VARIABLES_WITH_VALUES = {
                        "Overall Qual"   : list(range(10)),
                        ####
                        "Lot Shape"      : ["IR3", "IR2", "IR1", "Reg"],
                        "Utilities"      : ["ELO", "NoSeWa", "NoSewr", "AllPub"],
                        "Land Slope"     : ["Sev", "Mod", "Gtl"],
                        ####
                        "Exter Qual"     :  ["Po", "Fa", "TA", "Gd", "Ex"], 
                        "Exter Cond"     :  ["Po", "Fa", "TA", "Gd", "Ex"], 
                        ####
                        "Bsmt Qual"      : ["NA","Po","Fa","TA","Gd","Ex"], # basement quality
                        "Bsmt Exposure"  : ["NA", "No", "Mn", "Av", "Gd"], # Refers to walkout or garden level walls
                        "BsmtFin Type 1"  : ["NA", "Unf", "LwQ", "Rec", "BLQ", "ALQ", "GLQ"], # Rating of basement finished area
                        "BsmtFin Type 2"  : ["NA", "Unf", "LwQ", "Rec", "BLQ", "ALQ", "GLQ"], # Rating of basement finished area (if multiple types)
                        "Heating QC"      : ["Po", "Fa", "TA", "Gd", "Ex"], # Heating quality and condition
                        "Electrical"     : ["Mix", "FuseP", "FuseF", "FuseA", "SBrkr"], # Electrical system
                        "Kitchen Qual"    : ["Po", "Fa", "TA", "Gd", "Ex"], # Kitchen quality
                        "Functional"     : ["Sal", "Sev", "Maj2", "Maj1", "Mod",  "Min2", "Min1", "Typ"], # Home functionality
                        "Fireplace Qu"    : ["NA", "Po", "Fa", "TA", "Gd", "Ex"], # Fireplace quality
                        "Garage Finish"  : ["NA", "Unf", "RFn", "Fin"],
                        "Garage Qual"    : ["NA", "Po", "Fa", "TA", "Gd", "Ex"],
                        "Garage Cond"    : ["NA", "Po", "Fa", "TA", "Gd", "Ex"],
                        "Paved Drive"    : ["N", "P", "Y"],
                        "Pool QC"        : ["NA", "Po", "Fa", "TA", "Gd", "Ex"], # here I added category "Po"
                        "Fence"          : ["NA", "MnWw", "GdWo", "MnPrv", "GdPrv"]
                }