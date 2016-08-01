from __future__ import division
from time import time

import numpy as np
import matplotlib.pyplot as pl

from pyde.de import DiffEvol

class Model(object):
    def __init__(self, x):
        self.x = x

    def __call__(self, a, p0, f):
        return a*np.sin(p0+2*np.pi*self.x*f)

if __name__ == '__main__':
    niter = 250
    
    x = np.linspace(0,10,100)
    m = Model(x)
    y = m(2,1,0.25) + np.random.normal(0,0.5,size=x.size)

    de = DiffEvol(lambda pv: ((y-m(*pv))**2).sum(), [[1,3],[0,2],[0,4]], 50)

    ## Run n number of generations
    tstart = time()
    res = de.optimize(niter)
    print((time()-tstart) / niter)
    
    ## Or use as an iterator
    for res in de(2):
        print res

    pl.plot(x,y,'.k')
    pl.plot(x,m(*res[0]),'k')
    pl.show()
