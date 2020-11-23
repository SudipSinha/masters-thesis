__author__ = "Sudip Sinha"

from math import exp, sqrt


# @profile
def sp_asian_call(r: float,    # Market
                  s0: float, sigma: float, q: float,    # Underlying
                  k: float, t: float, am: bool=False,    # Derivative
                  mach_eps=65536 * (7/3 - 4/3 - 1), n: int=25, h: float=0., ub: bool=True    # Computation
                  ) -> list:
	"""Prices of an American Asian call option using the singular point method"""

	# Time period
	dt = t / n
	# Effective interest rate
	R = exp((r - q) * dt)

	# Up and down factors
	u = exp(sigma * sqrt(dt))
	d = 1. / u

	# Risk neutral probability, discounted by R
	p_u = (R * u - 1) / (u * u - 1) / R
	p_d = 1. / R - p_u

	if p_u < 0. or p_u > 1.:
		raise ValueError

	# Create the list for singular points
	sp = [[[]] * (i + 1) for i in range(n + 1)]

	# Singular points for N(n,0)
	a = s0/(n+1) * (1 - d**(n+1)) / (1-d)
	sp[n][0] = [(a, max(a - k, 0.))]

	# Singular points for N(n,n)
	a = s0/(n+1) * (1 - u**(n+1)) / (1-u)
	sp[n][-1] = [(a, max(a - k, 0.))]

	# Singular points for N(n,j)
	for j in range(1, n):
		a_min = s0 / (n+1) * ((1 - d**(n-j+1)) / (1-d) + d**(n-j-1) * (1 - u**j) / (1-u))
		a_max = s0 / (n+1) * ((1 - u**(j+1)) / (1-u) + u**(j - 1) * (1 - d**(n-j)) / (1-d))
		if k < a_min:
			sp[n][j] = [(a_min, a_min - k), (a_max, a_max - k)]
		elif k > a_max:
			sp[n][j] = [(a_min, 0), (a_max, 0)]
		else:
			sp[n][j] = [(a_min, 0), (k, 0), (a_max, a_max - k)]

	# Singular points for N(i,j) i != n
	for i in range(n-1, n-2, -1):

		for j in range(i+1):

			a_min = s0 / (i+1) * ((1 - d**(i-j+1)) / (1-d) + d**(i-j-1) * (1 - u**j) / (1-u))
			a_max = s0 / (i+1) * ((1 - u**(j+1)) / (1-u) + u**(j-1) * (1 - d**(i-j)) / (1-d))

			if a_min > a_max:
				(a_min, a_max) = (a_max, a_min)    # Jugaad


			sp[i][j] = sp_i_j

	return sp
