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
  
Create an instance

  de = DiffEvol(neg_lnprob, bounds, npop, ngen)

Run the minimizer

  de_res = de()
  
Initialize emcee with the final population

  sampler = emcee.EnsembleSampler(npop, ndim, lnprob)
  sampler.run_mcmc(de_res.population, 1000)

  
