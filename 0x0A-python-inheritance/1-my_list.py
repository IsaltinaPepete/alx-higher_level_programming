#!/usr/bin/python3 
"""Defines a my_list class"""


class MyList(list):
	"""A class"""
	def __ini__(self):
		"""Inicialize a object"""
		super().__init__()

	def def print_sorted(self):
		"""Print a sorted list"""
		print(sorted(self))
