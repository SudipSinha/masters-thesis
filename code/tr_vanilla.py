__author__ = "Sudip Sinha"

from math import exp, sqrt


def vanilla_call(r: float,    # Market
                 s0: float, sigma: float, q: float,    # Underlying
                 k: float, t: float, am: bool=True,   # Derivative
                 n: int=25    # Computation
                 ) -> list:
	"""Price of a American or European call."""

	dt = t / n
	R = exp((r - q) * dt)
	u = exp(sigma * sqrt(dt))

	# Risk neutral probability, discounted by R
	p_u = (R * u - 1) / (u * u - 1) / R
	p_d = 1. / R - p_u

	print('DEBUG: dt={dt}, R={R}, u={u}, p_u={p_u}'.format(dt=dt, R=R, u=u, p_u=p_u))

	tree = [[0] * (i+1) for i in range(n+1)]
	for j in range(n+1):
		tree[n][j] = max(s0 * u**(-n+2*j) - k, 0.)
	for i in range(n-1, -1, -1):
		for j in range(i+1):
			tree[i][j] = p_u * tree[i+1][j+1] + p_d * tree[i+1][j]
			if am:
				tree[i][j] = max(tree[i][j], max(s0 * u**(-i+2*j) - k, 0.))
	return tree
