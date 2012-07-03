import Pmf

def PmfMean(pmf):
	"""
	Finds the mean of a distribution from a Pmf
	Args:
		pmf
	Returns:
		floating point	
	"""
	sum_probabilities = 0
	for k, v in pmf.Items():
		print(k, v)
		sum_probabilities += k*v
	return sum_probabilities


def PmfVar(pmf, mean):
	"""
	Finds the variance of a distribution from a Pmf
	Args:
		pmf
	Returns:
		floating point	
	"""
	sum_deviations = 0
	for k, v in pmf.Items():
		sum_deviations += v*(k - mean)*(k - mean)
	return sum_deviations	

population_deathages = {67: 1000, 69: 984, 70: 1100, 78:1200, 79: 1099, 80: 999}
population_pmf = Pmf.MakePmfFromDict(population_deathages)
print population_pmf.d

deathages_mean = PmfMean(population_pmf)
deathages_variance = PmfVar(population_pmf, deathages_mean)

print "Deathages Mean: ", deathages_mean
print "Deathages Variance: ", deathages_variance

check_mean = population_pmf.Mean()
check_variance = population_pmf.Var()

print "Sanity Check Mean: ", check_mean
print "Sanity Check Variance: ", check_variance

