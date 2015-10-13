#!/usr/bin/env python
# coding: utf-8
# Made by Bjorn Heesakkers, https://www.constructors.nl/
# Script that uses laziness to generate the exam answer for PageRank.

import os
import sys
import numpy

# Make sure this thing is n by n!
# Transition probability matrix
matrix = [
    [0, 1, 0, 0],
    [0, 0.5, 0.5, 0],
    [0.25, 0.25, 0.25, 0.25],
    [0, 0.5, 0, 0.5],
]

N = len(matrix)
# Called lambda on the slides, teleportation rate
a = 0.8

# Update the matrix accounting for teleportation
for r in range(0, len(matrix)):
    for c in range(0, len(matrix[r])):
        matrix[r][c] = (a / N) + (1.0 - a) * matrix[r][c]


# To start at node B Pagerank use [0, 1, 0, 0] etc (you can start at any state)
x0 = numpy.array([1, 0, 0, 0])


def recurse(i, vector, matrix):
    vector = vector.dot(matrix)
    if i == 0:
        return
    i -= 1
    print vector
    return recurse(i, vector, matrix)

# The position in the results gives the PR for that Node. So the third
# number in the outputted array is the PR of Node C.
recurse(10, x0, numpy.array(matrix))
