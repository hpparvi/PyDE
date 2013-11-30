.. PyDE documentation master file, created by
   sphinx-quickstart on Mon Sep 23 16:00:28 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================
 Welcome to PyDE's documentation!
==================================


Introduction
------------

PyDE implements the Differential Evolution global optimizer by Storn & Price [Storn97]_.


Installation
------------
::

    python setup.py install [--user]


Basic usage
-----------

PyDE is straightforward to use. The optimizer is initialized with the function to
be optimized, parameter boundaries as [``npar``,2] array, and population size
``npop``. The optimization can be done using the ``optimize(ngen)`` method::

  from pyde.de import DiffEvol

  rbf = lambda pv: (1-pv[0])**2 + 100*(pv[1]-pv[0]**2)**2 
  
  de = DiffEvol(rbf, [[0,2],[0,2]], 20)
  de.optimize(50)
  
  print de.minimum_location, de.minimum_value

or the optimizer instance can be used as a generator::

  from pyde.de import DiffEvol

  rbf = lambda pv: (1-pv[0])**2 + 100*(pv[1]-pv[0]**2)**2 
  
  de = DiffEvol(rbf, [[0,2],[0,2]], 20)

  for i,res in enumerate(de(50)):
    print i, de.minimum_location, de.minimum_value

References
----------

.. [Storn97] Storn, R., Price, K., Journal of Global Optimization 11: 341--359, 1997


=====
 API
=====

.. autoclass:: pyde.de.DiffEvol
   :members:


====================
 Indices and tables
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


