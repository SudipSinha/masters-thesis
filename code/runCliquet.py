__author__ = "Sudip Sinha"

from cliquet import cliquet_sp


def run_cliquet_high(ms: list, d: int = 9) -> None:
	"""Display short results for a list of 'n's."""

	for m in ms:
		pr = cliquet_sp( r = 0.03, q = 0., sigma = 0.2,
		                 # sigma = [(0.05 + 0.04 * i) for i in range(1,9)],
		                 t = 5., m = m, N = 5,
		                 f_loc = 0., c_loc = 0.08,
		                 f_glob = 0.16, c_glob = float('inf'), h = 1e-6 )
		# print('m = {m:4}: price = {pr:.{d}f}'.format(d = d, m = m, pr = pr))


def run_cliquet_low(ms: list, d: int = 9) -> None:
	"""Display short results for a list of 'n's."""

	for m in ms:
		pr = cliquet_sp( r = 0.03, q = 0., sigma = 0.02,
		                 t = 5., m = m, N = 5,
		                 f_loc = 0., c_loc = 0.08,
		                 f_glob = 0.16, c_glob = float('inf'), h = 1e-6 )
		# print('m = {m:4}: price = {pr:.{d}f}'.format(d = d, m = m, pr = pr))


def run_cliquet_var(ms: list, d: int = 9) -> None:
	"""Display short results for a list of 'n's."""

	for m in ms:
		pr = cliquet_sp( r = 0.03, q = 0.,
		                 sigma = [(0.05 + 0.04 * i) for i in range(1,9)],
		                 t = 2., m = m, N = 8,
		                 f_loc = 0., c_loc = 0.08,
		                 f_glob = 0.16, c_glob = float('inf'), h = 0. )
		# print('m = {m:4}: price = {pr:.{d}f}'.format(d = d, m = m, pr = pr))
