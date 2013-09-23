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

    de = DiffEvol(minfun, bounds, npop)

where ``minfun`` is the function to be optimized, ``bounds`` is an initialization array, 
and ``npop`` is the size of the parameter vector population.

Now, you can run the optimizer ``ngen`` generations

::

    res = de.optimize(ngen=100)
  
or run the optimizer as an iterator
  
::

    for res in de(ngen=100):
        do something
  
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
:``F``:         Difference amplification factor. Values between 0.5-0.8 are good in most cases.
:``C``:         Cross-over probability. Use 0.9 to test for fast convergence, and smaller values (~0.1) for a more elaborate search.
:``seed``:      Random seed.
:``verbose``:   Verbosity.

**Returns**
