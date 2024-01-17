#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: angles_definition
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Script to define and explain the angles definition in winxray.
"""

###############################################################################
# Copyright 2023 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d

# Local modules.

# Project modules.

# Globals and constants variables.


def beam_sample_angles():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # beam
    v1 = np.array([0, 0, -3])

    ax.quiver(0, 0, 3, v1[0], v1[1], v1[2], color='b', arrow_length_ratio=0.1)

    # sample
    sample_size = 4
    p = Rectangle((-sample_size/2, -sample_size/2), sample_size, sample_size, alpha=0.5, color='g')
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3D Vector Plot')


if __name__ == '__main__':
    beam_sample_angles()

    plt.show()
