import math
import thinkstats

def Pumpkin(weights):
	mean = thinkstats.Mean(pumpkin_lengths)
	variance = thinkstats.Var(pumpkin_lengths, mean)
	stdiv = math.sqrt(variance)
	return mean, variance, stdiv

pumpkin_lengths = [1, 1, 1, 3, 3, 591]
mean, variance, stdiv = Pumpkin(pumpkin_lengths)
print "Mean: %s, var: %s, stdiv: %s" % (mean, variance, stdiv)