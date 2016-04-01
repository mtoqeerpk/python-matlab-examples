#!/usr/bin/env python3
"""
demo of need to use INTENT() in the Fortran code with f2py
as current versions of f2py assume INTENT(IN), which is an obvious
issue for getting results back to Python!

make
python3 f2py_demo.py

Note: You must use the f2py corresponding to your Python, 2 or 3

Note: imports from f2py will always be ALL lowercase!

Michael Hirsch
"""
import numpy as np
from pyprod import prod


x=3
y=2
#%%
zint = prod.prodintent(x,y)
assert zint == x*y
#%%
znoint = 12345.
znointent = prod.prodnointent(x,y,znoint)
assert znointent is None
assert np.isclose(znoint,12345.) #unmodified due to f2py intent(in) by default
#%%
zpure = prod.prodpure(x,y)
assert zpure == x*y
#%%
zinout = np.array(23456.) #MUST be an ndarray e.g. 0d ndarray for scalar case!
prod.prodinout(x,y,zinout)
assert zinout==x*y
