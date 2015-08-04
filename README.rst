**DaftHM** is a Python package, based on the `Daft <http://daft-pgm.org>`_ package authored by Dan Foreman-Mackey and David W. Hogg, that uses `matplotlib <http://matplotlib.org/>`_
to render pixel-perfect *probabilistic graphical models* for publication
in a journal or on the internet. With a short Python script and an intuitive
model-building syntax you can design directed and undirected graphs and save
them in any formats that matplotlib supports.

DaftHM extends the Daft package in the following ways:

- Nodes
  - Syntax is now similar to other hierarchical modeling methods, and added the option for "discrete", i.e. square-shaped, nodes
    - Primary ``Node`` class flags are ``observed``, ``fixed``, and ``continuous`` 
      - ``observed``: If ``False`` (default), node shape is shaded white, otherwise grey
      - ``fixed``: If ``False`` (default), node is single-bordered, other wise double-bordered,indicating that the value of the node is completely determined by it's ancestor nodes
      - ``continuous`: If ``True`` (default), node is a circle, otherwise node is a square, indicating a discrete value
