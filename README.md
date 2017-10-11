# CS510 CW 6

Julie Gardner-Hoag, Logan Gantner

Student ID: 2299636, 2307470

Email: gardnerh@chapman.edu, gantner@chapman.edu

Course: CS510 Fall 2017

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-06-logan_julie.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-06-logan_julie)

## Specification

1. Keeping your group of two (GROUPA), find another nearby group that you have not yet worked with (GROUPB). Link each other the repositories for the latest CW05, so that you can evaluate each other's code.
    * Open a Jupyter notebook: ```critique-GROUPA-GROUPB.ipynb```
    * Constructively critique GROUPB's code in your Jupyter notebook (in the GROUPA CW06 repository). Use the following questions as a guideline: Is it clear how the code is organized? Is the code properly documented with both docstrings and supplementary comments according to industry standards? Can you follow the algorithm of the code, i.e., what it is doing, and how? Do you see any suggestions for how to improve the code? Discuss your critique with the members of the other group.
    * Send each other your respective critique notebooks. Commit both your critique and their critique to your repository.
1. Work through the [Numpy/Pandas slides](http://slides.com/profdressel/numpy-and-pandas-overview) carefully. Be sure to use ```ipython3``` in a terminal to test how things work. Discuss amongst yourselves anything that is new or unclear.
1. Create a python module ```cplane-np.py```. Import the module ```abscplane.py``` in the repository. Create a new class ```ArrayComplexPlane``` that subclasses the abstract base class ```AbsComplexPlane```. Provide implementations for the requested methods similar to the last classwork, but instead use ```numpy``` arrays augmented with ```pandas``` labels to implement the 2D complex plane.  (Hint: Try to avoid using explicit ```for``` loops in your code. Instead use features of ```numpy``` to avoid ```for``` loops.)
1. Create a test module ```test_cplane-np.py``` that verifies that your implementation is correct.
1. In a Jupyter notebook ```cplane-np.ipynb``` provide a demonstration of how your class works (using small grids of points for clarity). Include a detailed discussion comparing this implementation with your previous implementation using vanilla python lists.
1. After your notebooks are complete, spell-checked, and professionally formatted properly, add and commit them to GitHub. Note that managing conflicts with Jupyter notebooks can be a pain, so I recommend having only one person from your edit the notebooks at a time, being sure to pull all changes before you start editing yourself.


## Assessment

This assignment taught us a lot about numpy and pandas. The biggest hurdle we had to get over was the issue of vectorizing our array and trying to apply our labels to it. We had to change our code to use pandas applymap method instead.

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Julie Gardner-Hoag, Logan Gantner