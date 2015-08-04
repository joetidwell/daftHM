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

This graphical model reproduces the example included in `Tom Lodewyckx's <https://sites.google.com/site/tomlodewyckx/downloads/TutorialGMLTX.zip?attredirects=0>`_ tutorial on making graphical models in LaTex, which itself is based on work by `Lee & Wagenmakers, 2009 <http://www.socsci.uci.edu/∼ mdlee/bgm.html>`_. 

The Plot
--------

.. image:: https://raw.github.com/joetidwell/daftHM/master/images/wagenmakers.png

The Code
--------

.. code-block:: python

  from matplotlib import rc
  rc("font", family="serif", size=14)
  rc("text", usetex=True)

  pgm = PGM(shape=[9, 8], origin=[0, 0], observed_style='shaded', node_unit=1.3)

  # Nodes
  pgm.add_node(Node(name="delta", content=r"$\delta$", x=3.5, y=7))
  pgm.add_node(Node(name="mu_alpha", content=r"$\mu_{\alpha}$", x=3, y=6, fixed=True))
  pgm.add_node(Node(name="sigma_alpha", content=r"$\sigma_{\alpha}$", x=4, y=6))
  pgm.add_node(Node(name="alpha_i", content=r"$\alpha_{i}$", x=3.5, y=5))
  pgm.add_node(Node(name="phi_SB", content=r"$\phi_{SB,i}$", x=3.5, y=4, fixed=True))
  pgm.add_node(Node(name="theta_SB", content=r"$\theta_{SB,i}$", x=3.5, y=3, fixed=True, continuous=False))
  pgm.add_node(Node(name="K_SB", content=r"$K_{SB,i}$", x=3.5, y=2, continuous=False, observed=True))
  pgm.add_node(Node(name="N_SB", content=r"$N_{SB,i}$", x=3.5, y=1, continuous=False, observed=True))
  pgm.add_node(Node(name="mu_phi", content=r"$\mu_{\phi}$", x=1, y=6))
  pgm.add_node(Node(name="sigma_phi", content=r"$\sigma_{\phi}$", x=2, y=6))
  pgm.add_node(Node(name="phi_SN", content=r"$\phi_{SN,i}$", x=1.5, y=4))
  pgm.add_node(Node(name="theta_SN", content=r"$\theta_{SN,i}$", x=1.5, y=3, fixed=True))
  pgm.add_node(Node(name="K_SN", content=r"$K_{SN,i}$", x=1.5, y=2, continuous=False, observed=True))
  pgm.add_node(Node(name="N_SN", content=r"$N_{SN,i}$", x=1.5, y=1, continuous=False, observed=True))

  #Edges
  pgm.add_edge("delta", "mu_alpha")
  pgm.add_edge("sigma_alpha", "mu_alpha")
  pgm.add_edge("sigma_alpha", "alpha_i")
  pgm.add_edge("mu_alpha", "alpha_i")
  pgm.add_edge("alpha_i","phi_SB")
  pgm.add_edge("alpha_i","phi_SB")
  pgm.add_edge("phi_SB","theta_SB")
  pgm.add_edge("theta_SB", "K_SB")
  pgm.add_edge("N_SB","K_SB")
  pgm.add_edge("sigma_phi", "phi_SN")
  pgm.add_edge("mu_phi", "phi_SN")
  pgm.add_edge("phi_SN","theta_SN")
  pgm.add_edge("theta_SN", "K_SN")
  pgm.add_edge("N_SN","K_SN")
  pgm.add_edge("phi_SN","phi_SB")

  #Plates
  pgm.add_plate(Plate([.5, .25, 4, 5.1], label=r"$i=1,\dots ,74$"))

  #Equations
  pgm.add_equation(Equation(r"$\delta \sim N(0,1)$",5.5, 7))

  pgm.add_equation(Equation(r"$\mu_{\phi} \sim |N(0,1)|$",5.5, 6.4))
  pgm.add_equation(Equation(r"$\sigma_{\phi} \sim U(0,10)$",5.5, 6.1))
  pgm.add_equation(Equation(r"$\mu_{\alpha} = \delta\sigma_{\alpha}$",5.5, 5.8))
  pgm.add_equation(Equation(r"$\sigma_{\alpha} \sim U(0,10)$",5.5, 5.5))

  pgm.add_equation(Equation(r"$\alpha_{i} \sim N(\mu_{\alpha},\sigma^2_{\alpha})$",5.5, 4.9))

  pgm.add_equation(Equation(r"$\phi_{SN,i} \sim N(\mu_{\phi},\sigma^2_{\phi})$",5.5, 4.1))
  pgm.add_equation(Equation(r"$\phi_{SB,i} = \phi_{SN,i}+\alpha_i$",5.5, 3.8))

  pgm.add_equation(Equation(r"$\theta_{SN,i} = \Phi (\phi_{SN,i})$",5.5, 3.1))
  pgm.add_equation(Equation(r"$\theta_{SB,i} = \Phi (\phi_{SB,i})$",5.5, 2.8))

  pgm.add_equation(Equation(r"$K_{SN,i} = \mbox{Binomial}(\theta_{SN,i},N_{SN,i})$",5.5, 2.1))
  pgm.add_equation(Equation(r"$K_{SB,i} = \mbox{Binomial}(\theta_{SB,i},N_{SB,i})$",5.5, 1.8))

  #Plot
  pgm.render()