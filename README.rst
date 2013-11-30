PyDE
====

Global optimization using differential evolution in Python [Storn97]_.


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

Now, you can run the optimizer ``ngen`` generations::

    res = de.optimize(ngen=100)
  
or run the optimizer as a generator::

    for res in de(ngen=100):
        do something
  
Usage with emcee
----------------

The PyDE parameter vector population can be used to initialize the affine-invariant MCMC sampler 
`emcee <http://dan.iel.fm/emcee/current/>`_ when a simple point estimate of the function minimum 
(or maximum) is not sufficient::

    de = DiffEvol(lnpost, bounds, npop, maximize=True)
    de.optimize(ngen)
    
    sampler = emcee.EnsembleSampler(npop, ndim, lnpost)
    sampler.run_mcmc(de.population, 1000)
 
References
----------
.. [Storn97] Storn, R., Price, K., Journal of Global Optimization 11: 341--359, 1997

  
API
---

*pyde.de.*\ **DiffEvol** (``minfun``, ``bounds``, ``npop``, ``F=0.5``, ``C=0.5``,
``seed=0``, ``maximize=False``)

**Parameters**

:``minfun``:    Function to be minimized.
:``bounds``:    Parameter space bounds as ``[npar,2]`` array.
:``npop``:      Size of the parameter vector population.
:``F``:         Difference amplification factor. Values between 0.5-0.8 are good in most cases.
:``C``:         Cross-over probability. Use 0.9 to test for fast convergence, and smaller values (~0.1) for a more elaborate search.
:``seed``:      Random seed.
:``maximize``:  An *optional* switch telling whether we want maximize or minimize the function. Defaults to minimization.
