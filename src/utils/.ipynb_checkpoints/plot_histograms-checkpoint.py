# ********************************************************************************** #
#                                                                                    #
#   Project: Data Frame Explorer                                                     #                         
#   Author: Pawel Rosikiewicz                                                        #
#   Contact: prosikiewicz(a)gmail.com                                                #
#                                                                                    #
#   License: MIT License                                                             #
#   Copyright (C) 2021.01.30 Pawel Rosikiewicz                                       #
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

from matplotlib import colors
import matplotlib.patches as patches





# Function, ......................................................
def plot_histograms(*, df, names, title=""):
    '''
        produce nice looking histograms for data in each column in input dataframe
        each histogram has unique color, thus it is easy to compare these histograms on different plots, 
        with different data transfomration methods
        - df;  dataframe or numpy array,
        - feature_names; list, len==df.shape[1]
        - title; str, use for fig.suptitle()
    '''

    df = pd.DataFrame(df)
    
    # prepare colorset, - can be used as cmap, 
    cmap = mpl.cm.get_cmap('tab10')
    rgba = cmap(np.linspace(0,1,len(names)))
    
    # Figure, 
    fig, axs = plt.subplots(
        nrows=1, 
        ncols=len(names), 
        figsize=(len(names)*2, 2), 
        facecolor="white"
    )

    # Subplots,
    for i, ax in enumerate(axs.flat):
        if i+1 > len(names): 
            break
    
        # hist
        fig.suptitle(title, fontsize=14)
        ax.hist(
            df.iloc[:,i], 
            bins=30, 
            color=rgba[i], 
            histtype="stepfilled", 
            edgecolor="black"
        )
        ax.set_title(names[i])
        ax.xaxis.set_major_locator(plt.MaxNLocator(2))
        ax.yaxis.set_major_locator(plt.MaxNLocator(3))
        sns.despine()

    # Aestetics, 
    plt.tight_layout() # to avoid overlapping with the labels
    plt.subplots_adjust(top=0.7)
    plt.show();
    