import math

import thinkstats
import survey
import Pmf

def ProbEarly(preglenghts):
	"""Args: pmf of preglengths
	Return: float """
	timing_bin = range(0, 37)
	return Timing_Risks(timing_bin, preglenghts)

def ProbOntime(preglenghts):
	"""Args: pmf of preglengths
	Return: float """
	timing_bin = range(37, 41)
	return Timing_Risks(timing_bin, preglenghts)

def ProbLate(preglenghts):
	"""Args: pmf of preglengths
	Return: float """
	timing_bin = range(41, 100) # Is there a better way to set the upper bound for a range?
	return Timing_Risks(timing_bin, preglenghts)

def Timing_Risks(bin, preglengths):
	sumbirths = 0
	for numweeks, probability in preglengths.Items():
		if numweeks in bin:
			sumbirths += probability
	risk = sumbirths/preglengths.Total()
	return risk

def Compile_Preglenths():
	table = survey.Pregnancies()
	table.ReadRecords()

	all_births = 0
	first_births = 0
	non_firsts = 0
	non_births = 0

	allbirths_dist = {}
	firstbirth_dist = {}
	nonfirst_dist = {}

	for rec in table.records:
		allbirths_dist.setdefault(rec.prglength, 0) # Create the key for that preglength if it doesn't exist yet
		firstbirth_dist.setdefault(rec.prglength, 0)
		nonfirst_dist.setdefault(rec.prglength, 0)

		if rec.outcome == 1:
			allbirths_dist[rec.prglength] +=1
			all_births +=1
			if rec.birthord == 1:
				firstbirth_dist[rec.prglength] += 1 
				first_births += 0
			if rec.birthord != 1:
				nonfirst_dist[rec.prglength] += 1 
				non_firsts += 1
		else:
			non_births +=1  


	allbirths_pmf = Pmf.MakePmfFromDict(allbirths_dist)
	firstbirth_pmf = Pmf.MakePmfFromDict(firstbirth_dist)
	nonfirst_pmf = Pmf.MakePmfFromDict(nonfirst_dist)

	return allbirths_pmf, firstbirth_pmf, nonfirst_pmf

early_bin = range(0, 37)	
ontime_bin = range(37, 41)
late_bin = range(41, 100)

allbirths, firstbirths, nonfirsts = Compile_Preglenths()

all_early_risk = ProbEarly(allbirths)
print "Early Risk for All Births: ", all_early_risk
all_ontime_risk = ProbOntime(allbirths)
print "Ontime Risk for All Births: ", all_ontime_risk
all_late_risk = ProbLate(allbirths)
print "Late Risk for All Births: ", all_late_risk

firstbirth_early_risk = ProbEarly(firstbirths)
print "Early Risk for Firstbirths: ", firstbirth_early_risk
firstbirth_ontime_risk = ProbOntime(firstbirths)
print "Ontime Risk for Firstbirths: ", firstbirth_ontime_risk
firstbirth_late_risk = ProbLate(firstbirths)
print "Late Risk for Firstbirths:", firstbirth_late_risk

nonfirst_early_risk = ProbEarly(nonfirsts)
print "Early Risk for Nonfirsts: ", nonfirst_early_risk
nonfirst_ontime_risk = ProbOntime(nonfirsts)
print "Ontime Risk for Nonfirsts: ", nonfirst_ontime_risk
nonfirst_late_risk = ProbLate(nonfirsts)
print "Late Risk for Nonfirsts:", nonfirst_late_risk

relative_firstbirth_early = firstbirth_early_risk / nonfirst_early_risk
relative_firstbirth_late = firstbirth_late_risk / nonfirst_late_risk

print "Relative risk that a first birth will be early: ", relative_firstbirth_early
print "Relative risk that a first birth will be late: ", relative_firstbirth_late
## On the above I got different answers from author. Probably due to how I did the bins for early/ontime/late

## 2.7, probability that someone starting 39th week of pregnancy
## will have birth next week

def Prob_next_week(preglengths, week):
	"""Args: preglength pmf and current week of preg.
	Return: float (probability of birth nextweek)
	"""
	shorter_pmf = Shorten_pmf(pmf, week)
	shorter_dist = shorter_pmf.Items()
	return shorter_dist[week]

def Shorten_pmf(preglengths, week):
	""" Args: preglength pmf and current week of preg.
	Return: pmf """
	for k, v in preglengths.Items():
		if k < week:
			preglengths.Remove(k)
	preglengths.Normalize()
	remaining_lengths = preglengths
	return remaining_lengths

shorter = Shorten_pmf(allbirths, 39)
shorter_dict = dict(shorter.Items())
print shorter_dict
print shorter_dict[39]