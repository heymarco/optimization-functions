try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
try:
    import builtins
except ImportError:
    # Python 2 compat: just to be able to declare that Python >=3.5 is needed.
    import __builtin__ as builtins

# This is a bit (!) hackish: we are setting a global variable so that the
# main skopt __init__ can detect if it is being loaded by the setup
# routine
builtins.__SKOPT_SETUP__ = True

import optifn

VERSION = optifn.__version__

CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7',
               'Programming Language :: Python :: 3.8']


setup(name='optimization-functions',
      version=VERSION,
      description='Common functions for testing optimization algorithms.',
      url='https://github.com/heymarco/optimization-functions',
      license='MIT',
      author='Marco Heyden',
      classifiers=CLASSIFIERS,
      packages=['optifn'],
      install_requires=["numpy"],
      extras_require={
        'plots':  ["matplotlib>=2.0.0"]
        }
      )
