#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python
import argparse


parser = argparse.ArgumentParser(description = 'Calculate radius of the circle', 
				 prog = 'My program', usage = '%(prog)s [options]')
parser.add_argument('-r','--radius', type = int, required = True, help='radius of the circle')



def main(*args):
	args = parser.parse_args(*args)
	print(args.radius)
main(['-r'])