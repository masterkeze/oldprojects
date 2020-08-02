#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot
a = numpy.zeros([3,2])
a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[2, 1] = 12

matplotlib.pyplot.imshow(a, interpolation="nearest")
print(a)
