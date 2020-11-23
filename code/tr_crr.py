__author__ = "Sudip Sinha"

from math import exp, sqrt


def tr_underlying(s0: float, sigma: float, t: float, n: int) -> list:
	"""Generate the tree of stock prices"""

	s = [[0] * (i+1) for i in range(n+1)]
	s[0][0] = s0

	dt = t / n
	u = exp(sigma * sqrt(dt))

	for i in range(1, n+1):
		for j in range(i+1):
			s[i][j] = s0 * u**(-i + 2*j)

	return s
