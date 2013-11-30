"""
Implements the differential evolution optimization method by Storn & Price
(Storn, R., Price, K., Journal of Global Optimization 11: 341--359, 1997)

.. moduleauthor:: Hannu Parviainen <hpparvi@gmail.com>
"""
from __future__ import division 

import numpy as np
from numpy.random import random, randint

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
    def __init__(self, fun, bounds, npop, F=0.5, C=0.5, seed=0, maximize=False):
        np.random.seed(seed)

        self.minfun = fun
        self.bounds = np.asarray(bounds)
        self.n_pop  = npop
        self.n_par  = (self.bounds).shape[0]
        self.bl = np.tile(self.bounds[:,0],[npop,1])
        self.bw = np.tile(self.bounds[:,1]-self.bounds[:,0],[npop,1])
        self.m  = -1 if maximize else 1

        self.seed = seed
        self.F = F
        self.C = C

        self._population = self.bl + random([self.n_pop, self.n_par]) * self.bw
        self._fitness    = np.zeros(npop)
        self._minidx     = None

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
        t = np.zeros(3, np.int)
        
        for i in xrange(self.n_pop):
            self._fitness[i] = self.m * self.minfun(self._population[i,:])

        for j in xrange(ngen):
            for i in xrange(self.n_pop):
                t[:] = i
                while  t[0] == i:
                    t[0] = randint(self.n_pop)
                while  t[1] == i or t[1] == t[0]:
                    t[1] = randint(self.n_pop)
                while  t[2] == i or t[2] == t[0] or t[2] == t[1]:
                    t[2] = randint(self.n_pop)
    
                v = self._population[t[0],:] + self.F * (self._population[t[1],:] - self._population[t[2],:])

                ## --- CROSS OVER ---
                crossover = random(self.n_par) <= self.C
                u = np.where(crossover, v, self._population[i,:])

                ## --- FORCED CROSSING ---
                ri = randint(self.n_par)
                u[ri] = v[ri].copy()

                ufit = self.m * self.minfun(u)
    
                if ufit < self._fitness[i]:
                    self._population[i,:] = u[:].copy()
                    self._fitness[i]      = ufit

            self._minidx = np.argmin(self._fitness)
            yield self.population[self._minidx,:], self._fitness[self._minidx]
