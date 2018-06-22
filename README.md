# An introduction to object-oriented programming in Python
## Hard-disks (as in 2D hard-spheres) dynamics simulations

These Jupyter notebooks form the basis of an intermediate course in programming taught at Imperial College's Department of Chemistry
to students following the degree in Chemistry with Molecular Physics. It assumes some familiarity with an imperative
programming style in Python (or another language, but Python basic syntax is not covered here) at the level of our
[introductory programming course](https://github.com/imperialchem/python-prog-intro).

The course serves also as an introduction to programming atomic/molecular computer simulations, by implementing a hard-disks
dynamics code as an illustration of object-oriented programming. **Note** that the simulation implementation is
(in some ways surprisingly) inefficient. There are better algorithms and programming approaches to solve this problem.
The choice here was to keep the algorithm simple, close to how general molecular dynamics algorithms work, and illustrating
the object oriented paradigm. Having said that, if you identify any obvious way in which the code could be made faster
without increasing its conceptual complexity, please [let us know](mailto:python@imperial.ac.uk).

The [1st notebook](https://github.com/imperialchem/python-prog-oo/blob/master/oo_workshop/oo_workshop.ipynb) offers
a brief overview of programming styles; motivates the use of an object-oriented paradigm; and covers the basic features
of object-oriented programming in Python.

The [2nd notebook](https://github.com/imperialchem/python-prog-oo/blob/master/oo_project/oo_project.ipynb) offers a step by step
guide to the implementation of a working object-oriented hard-sphere simulation program, and suggests some avenues for
exploring the simulation results.

The notebooks and related materials are made available under the [Creative Commons Attribution 4.0 (CC-by) license](https://creativecommons.org/licenses/by/4.0/),
and can be downloaded as a [zip archive](https://github.com/imperialchem/python-prog-oo/archive/master.zip).
In order to use the notebooks interactively in your computer you will need to have a python interpreter (version 3.x)
and the Jupyter notebook installed, both can be obtained, for example, by installing the [Anaconda](https://www.continuum.io/downloads) distribution.
