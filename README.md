PyDE
====

Differential evolution in Python.


Install
-------

    python setup.py install --user
  
Basic usage
-----------

Import the class from the package

    from pyde.de import DiffEvol
  
Create a DiffEvol instance

    de = DiffEvol(minfun, bounds, npop, ngen)

where minfun is the function to be minimized, bounds is an initialization array [[p1min, p1max], [p2min, p2max], ... [pnmin,pnmax]], npop is the size of the parameter vector population, and ngen the number of DE generations.

Run the minimizer

    de_res = de()
  
Usage with emcee
----------------

Simple, initialize emcee with the final DE population

    sampler.run_mcmc(de_res.population, 1000)

  
