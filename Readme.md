# Optimization Functions

This library includes different functions for testing optimization algorithms in python.

## Usage

you can either access the functions directly or use callable classes which implement the optimization function. In the latter case you have access to four different methods:

1. `type():` Returns the type of the function, either 'Many local minima', 'Bowl Shaped', 'Plate Shaped', or 'Valley Shaped'
2. `__call__(*args, **kwargs):` returns f(x)
3. `plot_2d():` shows a 2d-plot if possible
4. `eval_limits(dims: int = 2):` returns the usual evaluation limits according to sfu.ca/~ssurjano/index.html
5. `description():` prints additional information about the function

## Installation

Atm, you can add the library as a development library via pip:

    python -m pip install -e git+https://github.com/heymarco/optimization-functions.git#egg=optimization-functions --upgrade

## Thank you

Code and descriptions adopted from https://www.sfu.ca/~ssurjano/index.html