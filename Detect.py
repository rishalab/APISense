import argparse
import subprocess
import json
import os
from os import listdir
import sys

#Get all python files from given directory
def fileList(dirname):
	flist = listdir(dirname)
	flist = [fp for fp in flist if fp.find('.py')>0]
	flist = list(set([fp.split('.')[0].strip() for fp in flist]))
	return flist
	
#generates ASMs from Control flow Graphs
def generate_asm(dirname):
	flist = fileList(dirname)
	for fp in flist:
		#Subprocess executing pycfg file used to generating algorithm Control Flow Graphs
		subprocess.call(['python3','./pycfg-0.1/pycfg/pycfg.py',dirname+'/'+fp+'.py', '-c'])
		#Subprocess executing ASM generating algorithm implemented in Python
		subprocess.call(['python3','ASM.py',dirname+'/'+fp,dirname])
		os.remove(dirname+'/'+fp+'.txt')
	return



#Main funtion parsing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('testfiles', help='directory containing test dataset files or final result destination folder')
#parser.add_argument('-mu','--misuseInUsage', action='store_true', help='detects misuse in training dataset of usages')
#parser.add_argument('-mt','--misuseInTest', action='store_true', help='detects misuse in test dataset')
#parser.add_argument('-md','--misuseFdoc', action='store_true', help='detects misuse from API documentation')
args = parser.parse_args()
testfiles = args.testfiles
	
#Finding API misuse against contraint example of Documentation

if os.path.exists(testfiles):
	
	generate_asm(testfiles)
	testfp = fileList(testfiles)
	for fpt in testfp:
		subprocess.call(['python3', 'matching.py', 'ASMs/NoArg_patterns.txt', testfiles + '/' + fpt + '_asm.txt', ''])
		os.remove(testfiles + '/' + fpt + '_asm.txt')
		
		



		
