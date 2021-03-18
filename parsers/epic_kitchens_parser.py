import sys, os, csv, numpy as np

def main():
	# Args
	try:
		path_to_csv = sys.argv[1]
	except:
		print(f'Must have positional argument with path to csv:\n$ python3 {sys.argv[0]} /path/to/csv')

if __name__ == '__main__':
	main()