#!/usr/bin/env python
# coding: utf-8
# Made by Bjorn Heesakkers, https://www.constructors.nl/
# Script that uses naive Bayesian classifier to save us a lot of time
# on the trial exam

import os
import sys
from textblob.classifiers import NaiveBayesClassifier

train = [
    (
        'Japan earthquake', 'neg'
    ),
    (
        'News for bbc hints', 'pos'
    ),
    (
        'BBC kills off Robin Hood series', 'neg'
    ),
]


cl = NaiveBayesClassifier(train)

print cl.classify('Japan rocked by new earthquake')

print cl.classify('Nato raid\' kills Libyan rebels')

print cl.classify('Accelerator hints at new particle')

# Out of the above comes:
# neg
# neg
# pos

# While the real values are:
# pos
# neg
# pos

# Precision then is #relevant_retrieved / #retrieved
# 1 (the 3rd one) / 1 (only 1 doc retrieved) = 1
#
# Recall is #relevant_retrieved / #relevant
# 1 (the 3rd one) / 2 (the 1st and the 3rd doc) = 1/2.
