from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration
import distutils.sysconfig as ds

setup(name='PyDE',
      version='1.0',
      description='Differential Evolution in Python',
      author='Hannu Parviainen',
      author_email='hpparvi@gmail.com',
      url='',
      package_dir={'pyde':'src'},
      packages=['pyde']
     )
