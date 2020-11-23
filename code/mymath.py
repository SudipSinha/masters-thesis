# ==================================================================== #
__author__ = "Sudip Sinha"

from math import factorial


# -------------------------------------------------------------------- #

# @profile
def choose( n: int, r: int ):
	"""Number of ways of choosing r objects among n."""

	assert (type( n ) == int
	        and type( r ) == int and
	        0 <= r <= n), \
		"n = {n} and r = {r} must be non-negative integers".format(
		n = n, r = r )

	if r > (n / 2):
		r = n - r
	c = 1
	for i in range( n, n - r, -1 ):
		c *= i
	return c // factorial( r )

# ==================================================================== #
