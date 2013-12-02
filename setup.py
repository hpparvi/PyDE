from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration
import distutils.sysconfig as ds

with open('README.rst') as file:
    long_description = file.read()

setup(name='PyDE',
      version='1.0.1',
      description='Differential Evolution in Python',
      long_description=long_description,
      author='Hannu Parviainen',
      author_email='hpparvi@gmail.com',
      url='https://github.com/hpparvi/PyDE',
      package_dir={'pyde':'src'},
      packages=['pyde'],
      install_requires=["numpy"],
      license='GPLv2',
      classifiers=[
          "Topic :: Scientific/Engineering",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Developers",
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ]
     )
