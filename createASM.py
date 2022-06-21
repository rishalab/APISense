import argparse
import subprocess
import json
import os
from os import listdir
import sys

def fileList(dirname):
	flist = listdir(dirname)
	flist = [fp for fp in flist if fp.find('.py')>0]
	flist = list(set([fp.split('.')[0].strip() for fp in flist]))
	return flist

parser = argparse.ArgumentParser()
parser.add_argument('file', help='File for which ASM needs to be generated')
args = parser.parse_args()
dirname = args.file


flist = fileList(dirname)
for fp in flist:
	#Subprocess executing pycfg file used to generating algorithm Control Flow Graphs
	subprocess.call(['python3','./pycfg-0.1/pycfg/pycfg.py', dirname + '/' + fp + '.py', '-c'])
	#Subprocess executing ASM generating algorithm implemented in Python
	subprocess.call(['python3', 'ASM.py', dirname+'/' + fp, dirname])
	os.remove(dirname+'/'+fp+'.txt')
