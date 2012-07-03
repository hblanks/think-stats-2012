import Pmf
""" Given a PMF of deathage distributions and an age,
return a PMF of years remaining. 

Args: 
	Pmf object, int
Returns: 
	Pmf object
"""
def remaining_lifetime(deathages_pmf, age):
	# First turn the PMF into a histogram
	deathages = deathages_pmf.Items
	remaining = {}
	for deathyear, probability in deathages():
		years_from_death = deathyear-age
		remaining[years_from_death] = probability
	remaining_pmf = Pmf.MakePmfFromDict(remaining)
	return remaining_pmf
	

population_deathages = {67: 1000, 69: 984, 70: 1100, 78:1200, 79: 1099, 80: 9999}
population_pmf = Pmf.MakePmfFromDict(population_deathages)
renees_age = 26

renees_countdown = remaining_lifetime(population_pmf, renees_age)
print renees_countdown.d
