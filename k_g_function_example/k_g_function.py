__author__ = 'liyuanpeng'
import math
import logging
import numpy as np
from numpy import *


#given a k(x) function, for example, k(x)=\sqrt{|sin(x^3+2x)|}
def k_function(point):
    dimension = len(point)
    k_vector = np.zeros(dimension)
    for i in range(dimension):
        k_vector[i]=math.sqrt(np.absolute(sin(point[i] ** 3.0 + 2.0 * point[i])))

    return k_vector


def g_function(point):
    dimension = len(point)
    g_matrix = np.zeros([3, dimension])
    for i in range(dimension):
        # print np.dtype(point[i])
        g_matrix[0][i] = math.sqrt(np.absolute(sin(point[i] ** 2.0 + 2.0 * point[i])))
        g_matrix[1][i] = math.sqrt(np.absolute(cos(point[i] ** (5))))
        g_matrix[2][i] = np.absolute(tan(point[i] ** (3)))

    return g_matrix
