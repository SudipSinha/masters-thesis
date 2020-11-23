__author__ = "Sudip Sinha"

# import unittest
import tr_asian_singularpoints_old


# class SPAsianTest(unittest.TestCase):
#
# def setUp(self):
# 		r = 0.05
# 		n = 4
# 		eac = SPAsian.sp_asian_e_call(s0=100, k=90, sigma=0.5, q=0.0, n=n, t=1.0)
#
#
# 	def test_num_sp_nj_leq3(self):
# 		for j in range(n+1):
# 			self.assertTrue(len(eac[n][j]) <= 3, "Number of terminal singular points is greater than 3")
#
#
# 	def test_num_sp_i0_ii_eq1(self):
# 		for i in range(n+1):
# 			self.assertEqual(len(eac[i][0]), 1)
# 			self.assertEqual(len(eac[i][i]), 1)


r = 0.05
n = 4
eac = tr_asian_singularpoints_old.sp_asian_e_call(s0=100, k=90, sigma=0.5, q=0.0, t=1.0, n=n)


def test_num_sp_i0_ii_eq1(self):
	for i in range(n + 1):
		assert len(eac[i][0]) == 1
		assert len(eac[i][i]) == 1


def test_num_sp_nj_leq3():
	for j in range(n + 1):
		assert len(eac[n][j]) <= 3
