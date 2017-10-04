#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Logan Gantner
# Student ID: 2299636, 2307470
# Email: gardnerh@chapman.edu, gantner@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 6
###

import cplane_np as cplane
import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal

def f(z):
    return z+2

def test_plane():
    cPlane = cplane.ArrayComplexPlane(0,2,2,0,4,2)
    ans = pd.DataFrame([[0,2],[4j,2+4j]],index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(cPlane.plane, ans)

def test_apply():
    cPlane = cplane.ArrayComplexPlane(0,2,2,0,4,2)
    ans1 = pd.DataFrame([[0,2],[4j,2+4j]],index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(cPlane.plane, ans1, check_dtype=False)
    cPlane.apply(f)
    ans2 = pd.DataFrame([[2,4],[2+4j,4+4j]],index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(cPlane.plane, ans2, check_dtype=False)

def test_zoom():
    cPlane = cplane.ArrayComplexPlane(0,2,2,0,4,2)
    cPlane.apply(f)
    cPlane.zoom(1,2,2,1,2,2)
    ans = pd.DataFrame([[3+1j,4+1j],[3+2j,4+2j]],index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(cPlane.plane, ans)

def test_refresh():
    cPlane = cplane.ArrayComplexPlane(0,2,2,0,4,2)
    cPlane.apply(f)
    cPlane.refresh()
    ans = pd.DataFrame([[0,2],[4j,2+4j]],index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(cPlane.plane, ans)
