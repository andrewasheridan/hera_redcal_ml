import unittest
import numpy as np

from estdel_nn.data_creation import data_manipulation as dm

# test load_relevant_data
class test_dm_load_relevant_data(unittest.TestCase):

	# test __init__
	def test_data_paths_are_str(self):

		miriad_path = 1
		calfits_path = 2
		self.assertRaises(AssertionError, dm.load_relevant_data, miriad_path, calfits_path)

	