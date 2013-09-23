PyDE
====

Differential evolution in Python.


Installation
------------

::

    git clone https://github.com/hpparvi/PyDE.git
    cd PyDE
    python setup.py install [--user]
  
Basic usage
-----------

Import the class from the package

::

    from pyde.de import DiffEvol
  
Create a DiffEvol instance

::

    de = DiffEvol(minfun, bounds, npop, ngen)

where minfun is the function to be minimized, bounds is an initialization array [[p1min, p1max], [p2min, p2max], ... [pnmin,pnmax]], npop is the size of the parameter vector population, and ngen the number of DE generations.

Run the minimizer

::

    de_res = de()
  
Usage with emcee
----------------

Simple, initialize emcee with the final DE population

::

    sampler.run_mcmc(de_res.population, 1000)

  
API
---

*pyde.de.*\ **DiffEvol** (``minfun``, ``bounds``, ``npop``, ``ngen``, ``F=0.5``, ``C=0.5``,
``seed=0``, ``verbose=False``)

**Parameters**

:``minfun``:    Function to be minimized.
:``bounds``:    Parameter space bounds as [npar,2] array.
:``npop``:      Size of the parameter vector population.
:``ngen``:      Number of generations to run.
:``F``:         Difference amplification factor. Values between 0.5-0.8 are good in most cases.
:``C``:         Cross-over probability. Use 0.9 to test for fast convergence, and smaller values (~0.1) for a more elaborate search.
:``seed``:      Random seed.
:``verbose``:   Verbosity.

**Returns**
