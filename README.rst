Overview
========

**DaftHM** is a Python package, based on the `Daft <http://daft-pgm.org>`_ package authored by Dan Foreman-Mackey and David W. Hogg, that uses `matplotlib <http://matplotlib.org/>`_
to render pixel-perfect *probabilistic graphical models* for publication
in a journal or on the internet. With a short Python script and an intuitive
model-building syntax you can design directed and undirected graphs and save
them in any formats that matplotlib supports.


New Stuff
=========

DaftHM extends the Daft package in the following ways:

- Nodes
  - ``Node`` class code simplified 
  - Syntax is now similar to other hierarchical modeling methods, and added the option for "discrete", i.e. square-shaped, nodes
    - ``observed``: If ``False`` (default), node shape is shaded white, otherwise grey
    - ``fixed``: If ``False`` (default), node is single-bordered, other wise double-bordered,indicating that the value of the node is completely determined by it's ancestor nodes
    - ``continuous``: If ``True`` (default), node is a circle, otherwise node is a square, indicating a discrete value
- Plates
  - ``Plate`` class modified to replace ``matplotlib.patches.Rectangle`` with ``matplotlib.patches.FancyBboxPatch`` so plates have rounded corners by default
- Equations
  - Added ``Equation`` class and methods to enable inclusion of model equations in the plot

Example
=======

This graphical model reproduces the example included in `Tom Lodewyckx's <https://sites.google.com/site/tomlodewyckx/downloads/TutorialGMLTX.zip?attredirects=0>`_ tutorial on making graphical models in LaTex, which itself is based on a model developed by `Lee & Wagenmakers, 2009 <http://www.socsci.uci.edu/∼ mdlee/bgm.html>`_. 

The Plot
--------

.. image:: https://raw.github.com/joetidwell/daftHM/master/images/wagenmakers.png

The Code
--------

.. code-block:: python

import daftHM

