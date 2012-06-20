import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

first_births = 0
non_firsts = 0
non_births = 0

firstbirth_prglength_cumm = 0.0
nonfirst_prglength_cumm = 0.0

for rec in table.records:
  if rec.outcome == 1 and rec.birthord == 1:
    first_births +=1
    firstbirth_prglength_cumm += rec.prglength
  elif rec.outcome == 1 and rec.birthord != 1:
    non_firsts +=1   
    nonfirst_prglength_cumm += rec.prglength
  else: 
    non_births +=1  
    
firstbirth_prglength_avg = firstbirth_prglength_cumm / first_births
nonfirst_prglength_avg = nonfirst_prglength_cumm / non_firsts

print 'Number of first births: ', first_births
print 'Number of births that werent the first: ', non_firsts
print 'Number of live births (should be 9148): ', first_births + non_firsts
print 'Number of non-births: ', non_births
print 'Total (should be 13593):', first_births + non_firsts + non_births

print 'Average length of firstbirth pregnancies: ', firstbirth_prglength_avg
print 'Average length of non-firstbirth pregnancies: ', nonfirst_prglength_avg

# OK I got 38 weeks (9.5 mo) for both of them. That sounds reasonable, but I can't run the book's code to double-check...what's this thinkstats module? Also, the book references that we know the data in hours. How can that be...? Ohhhhh! They used floats instead of ints! So that's why they have partial months!