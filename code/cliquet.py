# ==================================================================== #
__author__ = "Sudip Sinha"

from math import exp, log, sqrt, ceil, floor, isclose
from mymath import choose


# -------------------------------------------------------------------- #

# @profile
def cliquet_sp( r: float, q: float, sigma: float, t: float,
                f_loc: float, c_loc: float, f_glob: float, c_glob: float,
                N: int, m: int, h: float = 0. ) -> float:
	"""Price of a cliquet option using the singular point method"""

	err_p = "ERROR: p_u must be a probability! " + \
	        "We must have dt < ( sigma ** 2 / ( r - q ) ** 2 ). " + \
	        "You may want to decrease the time interval."

	# Time period for each option
	n = m * N
	dt = t / n

	# Checks
	f_glob = max( N * f_loc, f_glob )
	c_glob = min( N * c_loc, c_glob )

	# Singular points for maturity (go to the nxt)
	now = [(N * f_loc, f_glob),
	       (f_glob, f_glob),
	       (c_glob, c_glob),
	       (N * c_loc, c_glob)]
	if f_glob == N * f_loc:
		now = now[1:]
	if c_glob == N * c_loc:
		now = now[:-1]

	# Uniqueness of sigma
	if type( sigma ) == float:
		unique_v = True
		assert dt < (sigma ** 2 / (r - q) ** 2), err_p
	elif type( sigma ) == list and len( sigma ) == N:
		unique_v = False
		sigma_list = sigma
	else:
		raise ValueError

	# Uniqueness of r
	if type( r ) == float:
		unique_r = True
	elif type( r ) == list and len( r ) == N:
		unique_r = False
		r_list = r
	else:
		raise ValueError

	# Unique f_loc and c_loc
	unique_fc = True

	if unique_r:
		# Effective interest rate for observable time periods
		R_N = exp( (r - q) * t / N )
		# Effective interest rate for computational time periods
		R_n = exp( (r - q) * t / n )

	if unique_v:
		u = exp( sigma * sqrt( dt ) )  # Up factor
	# d = 1. / u

	if unique_r and unique_v:
		# Risk neutral probability
		p_u = (R_n * u - 1) / (u * u - 1)
		p_d = 1. - p_u
		assert 0. <= p_u <= 1., err_p

	if unique_v and unique_r and unique_fc:
		# Possible range of return
		j_min = max( 0, floor(
			log( f_loc + 1 ) / (2 * sigma * sqrt( dt )) + m / 2 ) )
		j_max = min( m, ceil(
			log( c_loc + 1 ) / (2 * sigma * sqrt( dt )) + m / 2 ) )
		j0 = j_max - j_min

		# prb denotes p'
		prb = [0 for j in range( j0 + 1 )]
		prb[0] = 0
		for j in range( 0, j_min + 1 ):
			prb[0] += choose( m, j ) * (p_u ** j) * (p_d ** (m - j))
		prb[j0] = 0
		for j in range( j_max, m + 1 ):
			prb[j0] += choose( m, j ) * (p_u ** j) * (p_d ** (m - j))
		for j in range( j_min + 1, j_max ):
			prb[j - j_min] = choose( m, j ) * (p_u ** j) * (
			p_d ** (m - j))
		assert isclose( sum( prb ), 1. ), "Sum of PMF must be unity."

		# ret denotes R'
		ret = [0 for j in range( j0 + 1 )]
		ret[0] = f_loc
		ret[j0] = c_loc
		for j in range( j_min + 1, j_max ):
			ret[j - j_min] = u ** (-m + 2 * j) - 1

	# Come back from the nxt, one step at a time.
	for i in range( N - 1, -1, -1 ):
		nxt = now
		now = []

		# Checks
		if not unique_v or not unique_r:
			if not unique_r:
				r = r_list[i]
				# Effective interest rate for observable time periods
				R_N = exp( (r - q) * t / N )
				# Effective interest rate for computational time periods
				R_n = exp( (r - q) * t / n )
			if not unique_v:
				sigma = sigma_list[i]
				# Up factor
				u = exp( sigma * sqrt( dt ) )
				# Possible range of return
				j_min = max( 0, floor(
					log( f_loc + 1 ) / (
					2 * sigma * sqrt( dt )) + m / 2 ) )
				j_max = min( m, ceil(
					log( c_loc + 1 ) / (
					2 * sigma * sqrt( dt )) + m / 2 ) )
				j0 = j_max - j_min
			assert dt < (sigma ** 2 / (r - q) ** 2), err_p

			# Risk neutral probability
			p_u = (R_n * u - 1) / (u * u - 1)
			p_d = 1. - p_u
			assert 0. <= p_u <= 1., err_p

			# prb denotes p'
			prb = [0 for j in range( j0 + 1 )]
			prb[0] = 0
			for j in range( 0, j_min + 1 ):
				prb[0] += choose( m, j ) * (p_u ** j) * (p_d ** (m - j))
			prb[j0] = 0
			for j in range( j_max, m + 1 ):
				prb[j0] += choose( m, j ) * (p_u ** j) * (
				p_d ** (m - j))
			for j in range( j_min + 1, j_max ):
				prb[j - j_min] = choose( m, j ) * (p_u ** j) * (
				p_d ** (m - j))
			assert isclose( sum( prb ),
			                1. ), "Sum of PMF must be unity."

			# ret denotes R'
			ret = [0 for j in range( j0 + 1 )]
			ret[0] = f_loc
			ret[j0] = c_loc
			for j in range( j_min + 1, j_max ):
				ret[j - j_min] = u ** (-m + 2 * j) - 1

		# Obtain a sorted list for B
		b_list = []
		for l in range( 0, len( nxt ) ):
			for j in range( 0, j0 + 1 ):
				b = nxt[l][0] - ret[j]
				if (i * f_loc) <= b <= (i * c_loc):
					close = False
					for rsz in b_list:
						if isclose( rsz, b ):
							close = True
							break
					if not close:
						b_list.append( b )
		b_list = sorted( b_list )

		for b in b_list:
			v = 0
			for k in range( 0, j0 + 1 ):
				# Running sum Z corresponding to B at the nxt time step.
				rszp = b + ret[k]
				if rszp <= nxt[0][0]:
					vk = nxt[0][1]
				elif rszp >= nxt[-1][0]:
					vk = nxt[-1][1]
				else:
					for idx in range( 0, len( nxt ) ):
						if nxt[idx][0] <= rszp < nxt[idx + 1][0]:
							vk = (nxt[idx][1] +
							      (nxt[idx + 1][1] - nxt[idx][1]) /
							      (nxt[idx + 1][0] - nxt[idx][0]) *
							      (rszp - nxt[idx][0]))
				v += prb[k] * vk
			v /= R_N
			now.append( (b, v) )

		# Approximations
		if h > 0.:
			l = 0  # l is the starting index
			while l < len( now ) - 2:
				approx = True
				for j in range( len( now ) - 1, l + 1, -1 ):
					slope = (now[j][1] - now[l][1]) / (
					now[j][0] - now[l][0])
					for k in range( l + 1, j ):
						approx = True
						delta = abs(
							slope * (now[k][0] - now[l][0]) +
							now[l][1] - now[k][1] )
						if delta >= h:
							approx = False
							break
					if approx:
						break
				if approx and j > l + 1:
					del now[l + 1:j]
				l += 1

	return now[0][1]

# ==================================================================== #
