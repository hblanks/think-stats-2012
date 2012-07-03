# 2.2: Standard Deviation of Firsts, Others

import survey
import thinkstats
import math

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

first_births = 0
non_firsts = 0
non_births = 0

firstbirth_lengths = []
nonfirst_lengths = []

firstbirth_prglength_cumm = 0.0
nonfirst_prglength_cumm = 0.0

for rec in table.records:
  if rec.outcome == 1 and rec.birthord == 1: # Hunter suggests using nested if statements instead of "and" and elif
    first_births +=1
    firstbirth_lengths.append(rec.prglength)
    firstbirth_prglength_cumm += rec.prglength
  elif rec.outcome == 1 and rec.birthord != 1:
    non_firsts +=1   
    nonfirst_prglength_cumm += rec.prglength
    nonfirst_lengths.append(rec.prglength)
  else: 
    non_births +=1  
    
firstbirth_prglength_avg = firstbirth_prglength_cumm / first_births
firstbirth_prglength_variance = thinkstats.Var(firstbirth_lengths, firstbirth_prglength_avg)
firstbirth_prglength_stdv = math.sqrt(firstbirth_prglength_variance)

nonfirst_prglength_avg = nonfirst_prglength_cumm / non_firsts
nonfirst_prglength_variance = thinkstats.Var(nonfirst_lengths, nonfirst_prglength_avg)
nonfirst_prglength_stdv = math.sqrt(nonfirst_prglength_variance)

print 'Number of first births: ', first_births # Hunter suggests using %d, which lets you pass multiple arguments. Less messy when longer.
print 'Number of births that werent the first: ', non_firsts
print 'Number of live births (should be 9148): ', first_births + non_firsts
print 'Number of non-births: ', non_births
print 'Total (should be 13593):', first_births + non_firsts + non_births

print 'Average length of firstbirth pregnancies: ', firstbirth_prglength_avg
print 'Standard Deviation of firstbirth pregnancies: ', firstbirth_prglength_stdv

print 'Average length of non-firstbirth pregnancies: ', nonfirst_prglength_avg
print 'Standard Deviation of non-firstbirth pregnancies: ', nonfirst_prglength_stdv
print "Difference:", firstbirth_prglength_avg-nonfirst_prglength_avg