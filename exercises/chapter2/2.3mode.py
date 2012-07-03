import operator
import sys

import Pmf


entered = raw_input("Enter a sequence of integers you want to find the mode of (comma-seperated): ")
sequence = entered.split(", ")

hist = Pmf.MakeHistFromList(sequence)
histdict = hist.d 
print histdict

def Mode(hist):
	mode = None
	top_freq = 0

	for k, v in hist.iteritems():
		if v > top_freq:
			mode = k
			top_freq = v

	return mode

def AllModes(hist):
	sorted_hist = sorted(hist.iteritems(), reverse=True, key=operator.itemgetter(1)) 
	return sorted_hist

print Mode(histdict)		
print AllModes(histdict)