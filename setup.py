from setuptools import setup, find_packages


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
      description='Common functions for testing optimization algorithms.',
      url='https://github.com/heymarco/optimization-functions',
      license='MIT',
      author='Marco Heyden',
      classifiers=CLASSIFIERS,
      packages=find_packages("optimization-functions"),
      install_requires=["numpy"],
      extras_require={
        'plots':  ["matplotlib>=2.0.0"]
        }
      )
