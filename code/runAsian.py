__author__ = "Sudip Sinha"

from tr_crr import tr_underlying
from tr_vanilla import vanilla_call
from asian import asian_call_sp
from tr_asian_singularpoints_old import sp_asian_call_old


# http://www.goddardconsulting.ca/matlab-binomial-crr.html
# http://www.hoadley.net/options/binomialtree.aspx?tree=B
# http://www.mngt.waikato.ac.nz/kurt/frontpage/studentwork/danielchainov2003/bitree2.htm
# http://www.fintools.com/resources/online-calculators/options-calcs/binomial/
# http://www.optionspricevaluation.com/


def show_results(tree) -> None:
	s0 = 100.; k = 100.; sigma = 0.1; q = 0.; t = 0.25; r = 0.1; am = False; h = 1e-6

	# tree = tr_underlying(s0=s0, sigma=sigma, t=t, n=n)
	# eu = vanilla_call(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n)
	# sp = sp_asian_call_old(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=True, n=n)

	# print('n = {n}'.format(n=n))

	# print('\n' + '-' * 16 + '\tUnderlying tree \t' + '-' * 16)
	# # Display the tree for the underlying.
	# for (i, ti) in enumerate(tree):
	# 	print('N({i}): {ti}'.format(i=i, ti=ti))

	# print('\n' + '-' * 16 + '\tEuropean call   \t' + '-' * 16)
	# # Display the tree for the European call.
	# for (i, ti) in enumerate(eu):
	# 	print('N({i}): {ti}'.format(i=i, ti=ti))

	display = '\n' + '-' * 16 + '\tSingular points \t' + '-' * 16 + '\n'
	# Print the price of the Asian call.
	for (i, ti) in enumerate(tree):
		for (j, tj) in enumerate(ti):
			display = 'N({i},{j}): {tj}\n'.format(i=i, j=j, tj=tj) + display
		display = '-' * 64 + '\n' + display
	print(display)
	# print('Price of the call = {prc}'.format(prc=sp[0][0][0][1]))


def run_asian_old(ns: list, d: int=6) -> None:
	"""Display short results for a list of 'n's."""

	s0 = 100.; k = 90.; sigma = 0.2; q = 0.03; t = 1.; r = 0.1; am = True; h = 1e-6    # Table 1

	for n in ns:
		upper = sp_asian_call_old(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n, h=h, ub=True)[0][0][0][1]
		lower = sp_asian_call_old(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n, h=h, ub=False)[0][0][0][1]
		if n < 25:
			actual = sp_asian_call_old(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n)[0][0][0][1]
			print('n={n:3}: {lb:.{d}f} <= {ac:.{d}f} <= {ub:.{d}f}'.format(d=d, n=n, lb=lower, ac=actual, ub=upper))
		else:
			print('n={n:3}: {lb:.{d}f} <= {ub:.{d}f}'.format(d=d, n=n, lb=lower, ub=upper))


def run_asian(ns: list, d: int=6) -> None:
	"""Display short results for a list of 'n's."""

	# s0 = 100.; k = 100.; sigma = 0.1886; q = 0.; t = 0.25; r = 0.05; am = True; h = 1e-6    # Table 4

	# s0 = 100.; k = 90.; sigma = 0.2; q = 0.03; t = 1.; r = 0.1; am = True; h = 1e-6    # Table 1
	# s0 = 100.; k = 90.; sigma = 0.4; q = 0.03; t = 1.; r = 0.1; am = True; h = 1e-6    # Table 1
	s0 = 100.; k = 110.; sigma = 0.2; q = 0.03; t = 1.; r = 0.1; am = True; h = 1e-6    # Table 2
	# s0 = 100.; k = 110.; sigma = 0.2; q = 0.03; t = 1.; r = 0.1; am = True; h = 1e-6    # Table 2

	for n in ns:
		upper = asian_call_sp(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n, h=h, ub=True)
		lower = asian_call_sp(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n, h=h, ub=False)
		# if n < 25:
		# 	actual = asian_call_sp(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n)
		# 	print('n={n:3}: {lb:.{d}f} <= {ac:.{d}f} <= {ub:.{d}f}'.format(d=d, n=n, lb=lower, ac=actual, ub=upper))
		# else:
		print('{n:3}: {lb:.{d}f} <= {ub:.{d}f}'.format(d=d, n=n, lb=lower, ub=upper))
		# actual = asian_call_sp(r=r, s0=s0, sigma=sigma, q=q, k=k, t=t, am=am, n=n)
		# print('n={n:3}: {ac}'.format(d=d, n=n, ac=actual))


run_asian([25])
run_asian_old([25])

# run_asian([221], d=6)
# run_asian([222], d=6)
