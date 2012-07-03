import math

import survey
import thinkstats

table = survey.Pregnancies()
table.ReadRecords()

first_births = 0
non_firsts = 0
non_births = 0

firstbirth_lengths = []
nonfirst_lengths = []

firstbirth_prglength_cumm = 0.0
nonfirst_prglength_cumm = 0.0

for rec in table.records:
  if rec.outcome == 1 and rec.birthord == 1:
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

print 'Standard Deviation of firstbirth pregnancies: ', firstbirth_prglength_stdv
print 'Standard Deviation of non-firstbirth pregnancies: ', nonfirst_prglength_stdv
print "Difference:", firstbirth_prglength_avg-nonfirst_prglength_avg