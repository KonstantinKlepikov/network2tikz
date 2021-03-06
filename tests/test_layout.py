#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# =============================================================================
# File      : test_layout.py
# Creation  : 17 July 2018
# Time-stamp: <Son 2018-07-29 15:51 juergen>
#
# Copyright (c) 2018 Jürgen Hackl <hackl@ibi.baug.ethz.ch>
#               http://www.ibi.ethz.ch
# $Id$
#
# Description : Test functions for converting cnet networks to tikz-networks
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# =============================================================================

import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from network2tikz import plot
from network2tikz.layout import Layout, layout
import cnet as cn


@pytest.fixture
def net():
    net = cn.Network(name='my tikz test network', directed=True)
    net.add_edges_from([('ab', 'a', 'b'), ('ac', 'a', 'c'), ('cd', 'c', 'd'),
                        ('de', 'd', 'e'), ('ec', 'e', 'c'), ('cf', 'c', 'f'),
                        ('fa', 'f', 'a'), ('fg', 'f', 'g'), ('gd', 'g', 'd'),
                        ('gg', 'g', 'g')])
    net.edges['ab']['force'] = 3
    net.edges['ac']['force'] = 2
    net.edges['cd']['force'] = 1
    net.edges['de']['force'] = 1
    net.edges['ec']['force'] = 3
    net.edges['cf']['force'] = 1
    net.edges['fa']['force'] = 1
    net.edges['fg']['force'] = 1
    net.edges['gd']['force'] = 1
    net.edges['gg']['force'] = 1

    net.nodes['name'] = ['Alice', 'Bob', 'Claire', 'Dennis', 'Esther', 'Frank',
                         'George']
    net.nodes['age'] = [25, 31, 18, 47, 22, 23, 50]
    net.nodes['gender'] = ['f', 'm', 'f', 'm', 'f', 'm', 'm']

    net.edges['is_formal'] = [False, False, True, True, True, False, True,
                              False, False, False]
    return net


@pytest.fixture
def net2():
    nodes = ['a', 'b', 'c']
    edges = [('a', 'b'), ('b', 'c')]
    return nodes, edges


def test_visual_style(net2):

    visual_style = {}
    visual_style['layout'] = {'a': (0, 0), 'b': (0, 0), 'c': (0, 0)}
    visual_style['keep_aspect_ratio'] = False
    #plot(net, **visual_style)

    visual_style = {}
    visual_style['layout'] = {'a': (0, 0), 'b': (0, 0), 'c': (1, 0)}
    visual_style['keep_aspect_ratio'] = False
    #plot(net, **visual_style)

    visual_style = {}
    visual_style['layout'] = {'a': (0, 0), 'b': (0, 0), 'c': (0, 1)}
    visual_style['keep_aspect_ratio'] = False
    #plot(net, **visual_style)


def test_fruchterman_reingold(net):
    net.summary()
    A = net.adjacency_matrix().todense()
    print(A.shape)
    #L = Layout(net)
    # layout = L._fruchterman_reingold(A)

    # print(layout)
    _layout = {'a': (0, 0), 'b': (1, 1), 'c': (2, 2),
               'd': (3, 3), 'e': (4, 4), 'f': (5, 5), 'g': (6, 6)}

    layout_style = {}
    layout_style['layout'] = 'fr'
    layout_style['layout_seed'] = 1
    layout_style['layout_weight'] = 'force'
    _layout = layout(net, **layout_style)

    visual_style = {}
    visual_style['node_label_as_id'] = True
    visual_style['layout'] = _layout
    visual_style['canvas'] = (10, 10)
    visual_style['margin'] = 1
    plot(net, **visual_style)

    visual_style = {}
    visual_style['node_label_as_id'] = True
    visual_style['canvas'] = (10, 10)
    visual_style['margin'] = 1
    visual_style['layout'] = 'fr'  # _layout
    visual_style['layout_seed'] = 1
    visual_style['layout_weight'] = 'force'
    plot(net, **visual_style)


# =============================================================================
# eof
#
# Local Variables:
# mode: python
# mode: linum
# mode: auto-fill
# fill-column: 80
# End:
