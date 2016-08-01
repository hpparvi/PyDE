"""
Implements the differential evolution optimization method by Storn & Price
(Storn, R., Price, K., Journal of Global Optimization 11: 341--359, 1997)

.. moduleauthor:: Hannu Parviainen <hpparvi@gmail.com>
"""
from __future__ import division 

import math as mt
import numpy as np
from numpy.random import random, randint
from .de_f import de_f

def wrap(v, vmin, vmax):
    w = vmax-vmin
    return vmin+np.mod(np.asarray(v)-vmin, w)

class DiffEvol(object):
    """
    Implements the differential evolution optimization method by Storn & Price
    (Storn, R., Price, K., Journal of Global Optimization 11: 341--359, 1997)
    
    :param fun:
       the function to be minimized

    :param bounds:
        parameter bounds as [npar,2] array

    :param npop:
        the size of the population (5*D - 10*D)

    :param  F: (optional)
        the difference amplification factor. Values of 0.5-0.8 are good in most cases.

    :param C: (optional)
        The cross-over probability. Use 0.9 to test for fast convergence, and smaller
        values (~0.1) for a more elaborate search.

    :param seed: (optional)
        Random seed

    :param maximize: (optional)
        Switch setting whether to maximize or minimize the function. Defaults to minimization.
    """ 
    def __init__(self, fun, bounds, npop, periodic=[], F=None, C=None, seed=None, maximize=False, vfun=False, cbounds=[0.25, 1], fbounds=[0.25, 0.75], pool=None, min_ptp=1e-2):
        if seed is not None:
            np.random.seed(seed)
            
        self.minfun = fun
        self.bounds = np.asarray(bounds)
        self.n_pop  = npop
        self.n_par  = (self.bounds).shape[0]
        self.bl = np.tile(self.bounds[:,0],[npop,1])
        self.bw = np.tile(self.bounds[:,1]-self.bounds[:,0],[npop,1])
        self.m  = -1 if maximize else 1
        self.pool = pool

        if self.pool is not None:
            self.map = self.pool.map
        else:
            self.map = map

        self.periodic = []
        self.min_ptp = min_ptp
        
        self.cmin = cbounds[0]
        self.cmax = cbounds[1]
        self.cbounds = cbounds
        self.fbounds = fbounds
        
        self.seed = seed
        self.F = F
        self.C = C

        self._population = np.asarray(self.bl + random([self.n_pop, self.n_par]) * self.bw)
        self._fitness    = np.zeros(npop)
        self._minidx     = None

        self._trial_pop  = np.zeros_like(self._population)
        self._trial_fit  = np.zeros_like(self._fitness)

        if vfun:
            self._eval = self._eval_vfun
        else:
            self._eval = self._eval_sfun

    @property
    def population(self): 
        """The parameter vector population"""
        return self._population

    @property
    def minimum_value(self):
        """The best-fit value of the optimized function"""
        return self._fitness[self._minidx]

    @property
    def minimum_location(self):
        """The best-fit solution"""
        return self._population[self._minidx,:]

    @property
    def minimum_index(self):
        """Index of the best-fit solution"""
        return self._minidx
    
    def optimize(self, ngen):
        """Run the optimizer for ``ngen`` generations"""
        for res in self(ngen):
            pass
        return res

    def __call__(self, ngen=1):
        return self._eval(ngen)

    def _eval_sfun(self, ngen=1):
        """Run DE for a function that takes a single pv as an input and retuns a single value."""
        popc, fitc = self._population, self._fitness
        popt, fitt = self._trial_pop, self._trial_fit
        
        for ipop in range(self.n_pop):
            fitc[ipop] = self.m * self.minfun(popc[ipop,:])

        for igen in range(ngen):
            F = self.F or np.random.uniform(*self.fbounds)
            C = self.C or np.random.uniform(*self.cbounds)

            popt[:,:] = de_f.evolve_population(popc, F, C)

            for pid in self.periodic:
                popt[:,pid] = wrap(popt[:,pid], self.bounds[pid,0], self.bounds[pid,1])
            
            fitt[:] = self.m * np.array(self.map(self.minfun, popt))
            
            msk = fitt < fitc
            popc[msk,:] = popt[msk,:]
            fitc[msk]   = fitt[msk]

            self._minidx = np.argmin(fitc)

            if fitc.ptp() < self.min_ptp:
                break
            
            yield popc[self._minidx,:], fitc[self._minidx]


    def _eval_vfun(self, ngen=1):
        """Run DE for a function that takes the whole population as an input and retuns a value for each pv."""
        popc, fitc = self._population, self._fitness
        popt, fitt = self._trial_pop, self._trial_fit

        fitc[:] = self.m * self.minfun(self._population)

        for igen in range(ngen):
            #x = float(ngen-igen)/float(ngen)

            self.F = np.random.uniform(*self.fbounds)
            self.C = np.random.uniform(*self.cbounds)
            #self.C = x*self.cmax + (1-x)*self.cmin

            popt[:,:] = de_f.evolve_population(popc, self.F, self.C)
            fitt[:] = self.m * self.minfun(popt)
            msk = fitt < fitc
            popc[msk,:] = popt[msk,:]
            fitc[msk]   = fitt[msk]

            self._minidx = np.argmin(fitc)
            yield popc[self._minidx,:], fitc[self._minidx]

